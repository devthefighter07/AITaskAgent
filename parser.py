# parser.py

from docx import Document
import os

# List of action-related keywords to identify task-like sentences
TASK_KEYWORDS = ["develop", "create", "build", "implement", "setup", "design", "integrate", "deploy", "test", "support", "manage"]

def extract_tasks_from_docx(file_path):
    if not file_path.endswith(".docx") or not os.path.exists(file_path):
        raise FileNotFoundError("Invalid or missing .docx file.")

    doc = Document(file_path)
    full_text = " ".join([para.text.strip() for para in doc.paragraphs if para.text.strip()])
    sentences = full_text.split(".")  # naive sentence split

    tasks = []
    for sentence in sentences:
        lower_sentence = sentence.lower()
        if any(keyword in lower_sentence for keyword in TASK_KEYWORDS):
            clean = sentence.strip().replace("\n", " ")
            if clean:
                tasks.append(clean)

    return tasks
