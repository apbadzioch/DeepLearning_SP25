# rl/feedback.py

class FeedbackManager:
    def __init__(self):
        self.history = []

    def record_action(self, action_type, outcome):
        self.history.append({"action": action_type, "result": outcome})
        print("✅ Feedback recorded.")
