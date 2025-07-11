# scheduler.py

import schedule
import time
from main import run_pipeline

def schedule_daily_task():
    schedule.every().day.at("11:03").do(run_pipeline)

    print("⏰ Task scheduler is running daily... (Press Ctrl+C To Stop)")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    schedule_daily_task()
