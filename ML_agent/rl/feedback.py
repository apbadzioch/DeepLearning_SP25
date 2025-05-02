# rl/feedback.py
# Author: Andrew Badzioch
# Prupose: Simulated reinforcement learning component that logs agent actions
# and their outcomes for performance tracking and future policy improvement.

# rl/feedback.py
# Author: Andrew Badzioch
# Purpose: Simulated reinforcement learning component that logs agent actions
# and their outcomes for performance tracking and future policy improvement.

import json
import os
from datetime import datetime

class FeedbackManager:
    def __init__(self, logfile="logs/interaction_log.json"):
        self.history = []
        self.logfile = logfile
        os.makedirs(os.path.dirname(self.logfile), exist_ok=True)

    def record_action(self, action_type, outcome):
        record = {
            "timestamp": datetime.now().isoformat(),
            "action": action_type,
            "result": outcome
        }

        self.history.append(record)

        # Write to JSON file
        if os.path.exists(self.logfile):
            with open(self.logfile, "r") as f:
                data = json.load(f)
        else:
            data = []

        data.append(record)

        with open(self.logfile, "w") as f:
            json.dump(data, f, indent=4)

        print("✅ Feedback recorded and saved to log.")

