import csv
from datetime import datetime


def log_metrics(filename, eou_delay, ttft, ttfb, total_latency):
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                datetime.now().isoformat(),
                f"{eou_delay:.3f}",
                f"{ttft:.3f}",
                f"{ttfb:.3f}",
                f"{total_latency:.3f}",
            ]
        )


def log_usage_summary(filename, session_id, status):
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), session_id, status])
