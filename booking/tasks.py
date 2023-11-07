# summarizer/tasks.py
from celery import shared_task
import time

@shared_task
def summarize_text(text):
    # Simulate a long-running task
    time.sleep(3600)  # Sleep for 1 hour (3600 seconds)
    # Actual text summarization logic can be added here
    return "Summary of the text..."
