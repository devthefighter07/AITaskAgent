# main.py

from parser import extract_tasks_from_docx
from assigner import load_employee_emails, assign_tasks
from emailer import send_email

# 🔐 Email Credentials (Gmail + App Password only)
SENDER_EMAIL = "Test@gmail.com"
SENDER_PASSWORD = "****"  # Use your App Password

def run_pipeline():
    print("🚀 Running daily task automation...")

    # Step 1: Extract tasks from DOCX
    try:
        tasks = extract_tasks_from_docx("documents/project_definition.docx")
        if not tasks:
            print("⚠️ No tasks found in the document.")
            return
    except Exception as e:
        print(f"❌ Failed to extract tasks: {e}")
        return

    # Step 2: Load employee list from Excel
    try:
        employees = load_employee_emails("config/employee_emails.xlsx")
        if not employees:
            print("⚠️ No employees found to assign tasks.")
            return
    except Exception as e:
        print(f"❌ Failed to load employee list: {e}")
        return

    # Step 3: Assign tasks (round-robin)
    assigned_tasks = assign_tasks(tasks, employees)

    # Step 4: Send task emails
    for task in assigned_tasks:
        body = f"""Hello {task['Employee']},

                You have been assigned the following task:

                📝 Task: {task['Task']}
                📅 Due Date & Time: {task['Due Date']}

                Please confirm once done.

                Best,
                TaskBot
"""
        try:
            send_email(
                recipient_email=task["Email"],
                subject="🛠️ New Task Assigned",
                body=body,
                sender_email=SENDER_EMAIL,
                sender_password=SENDER_PASSWORD
            )
        except Exception as e:
            print(f"❌ Failed to send email to {task['Email']}: {e}")

    print("✅ All tasks assigned and emails sent.")

# Run manually if needed
if __name__ == "__main__":
    run_pipeline()
