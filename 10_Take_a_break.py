import time
from plyer import notification

def send_break_notification():
    """
    Sends a desktop notification reminding the user to take a break.
    """
    notification.notify(
        title="Time to Take a Break!",
        message="You've been working for a while. It's time to rest your eyes and stretch.",
        timeout=10  # The notification will stay for 10 seconds
    )

def main():
    break_interval = 30 * 60  # 30 minutes (in seconds)

    while True:
        send_break_notification()  # Send the notification
        print("Notification sent. Next reminder in 30 minutes.")
        
        # Wait for the specified interval before sending the next notification
        time.sleep(break_interval)

if __name__ == "__main__":
    main()
