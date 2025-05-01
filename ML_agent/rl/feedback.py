# rl/feedback.py
# Author: Andrew Badzioch
# Prupose: Simulated reinforcement learning component that logs agent actions
# and their outcomes for performance tracking and future policy improvement.

class FeedbackManager:
    def __init__(self):
        self.history = []

    def record_action(self, action_type, outcome):
        self.history.append({"action": action_type, "result": outcome})
        print("✅ Feedback recorded.")
