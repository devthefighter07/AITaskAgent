# assigner.py

import pandas as pd
import itertools
from datetime import datetime, timedelta

def load_employee_emails(excel_path="config/employee_emails.xlsx"):
    try:
        df = pd.read_excel(excel_path)
        employees = list(df.itertuples(index=False, name=None))  # (Name, Email)
        return employees
    except Exception as e:
        print(f"❌ Failed to read employee email sheet: {e}")
        return []

def assign_tasks(tasks, employees):
    import itertools
    if not tasks or not employees:
        return []

    employee_cycle = itertools.cycle(employees)
    now = datetime.now()

    assignments = []
    for i, task in enumerate(tasks):
        employee = next(employee_cycle)
        # Add time by default (e.g., 9:00 AM)
        due_datetime = now + timedelta(days=i % 5 + 1)
        due_str = due_datetime.strftime("%d-%b-%Y %I:%M %p")  # e.g., 09-Jul-2025 09:00 AM

        assignments.append({
            "Task": task,
            "Employee": employee[0],
            "Email": employee[1],
            "Due Date": due_str
        })

    return assignments