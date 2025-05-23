# tools/calendar_tool.py
# Author: Epoch Explorers
# Purpose: Simulates a calendar scheduling tool by managing a list of local events
# and checking for conflicts.

 
import datetime
import logging

class CalendarTool:
    def __init__(self):
        self.calendar = []  # Simulated list of calendar events

    def events_overlap(self, start1, end1, start2, end2):
        return max(start1, start2) < min(end1, end2)
    
    def schedule_event(self, title, date_str, time_str, duration_minutes=30):
        try:
            # Parse date and time
            event_datetime = datetime.datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
            end_time = event_datetime + datetime.timedelta(minutes=duration_minutes)

            for existing in self.calendar:
                existing_start = datetime.datetime.fromisoformat(existing["start"])
            # Simulated event creation
            event = {
                "title": title,
                "start": event_datetime.isoformat(),
                "end": end_time.isoformat()
            }

            # Check for conflicts
            for existing in self.calendar:
                if existing['start'] <= event['start'] <= existing['end']:
                    return f"❌ Conflict: '{title}' overlaps with another event."

            self.calendar.append(event)
            logging.info(f"Scheduled event: {event}")
            return f"✅ Event '{title}' scheduled on {date_str} at {time_str}."

        except Exception as e:
            logging.error(f"Calendar scheduling error: {str(e)}")
            return f"❌ Failed to schedule event: {str(e)}"
