import time
from plyer import notification

def set_reminder(title, message, delay):
    time.sleep(delay)  # Wait for the specified time
    notification.notify(
        title=title,
        message=message,
        timeout=10  # The notification will stay for 10 seconds
    )

# Example usage
set_reminder("Hydration Alert", "Drink a glass of water!", 10)  # Reminder in 10 seconds
