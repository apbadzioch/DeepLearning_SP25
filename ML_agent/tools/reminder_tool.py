# tools/reminder_tool.py
# Author: Andrew Badzioch
# Purpose: Simulates a reminder scheduling tool by logging reminders to memory.
 
import datetime
import logging

class ReminderTool:
    def __init__(self):
        self.sent_reminders = []

    def send_reminder(self, recipient, message, scheduled_time):
        try:
            # Simulate sending a reminder
            reminder = {
                "recipient": recipient,
                "message": message,
                "time": scheduled_time
            }

            self.sent_reminders.append(reminder)
            logging.info(f"Reminder sent to {recipient} for {scheduled_time}")
            return f"✅ Reminder scheduled for {recipient} at {scheduled_time}."
        except Exception as e:
            logging.error(f"Reminder error: {str(e)}")
            return f"❌ Failed to schedule reminder: {str(e)}"
