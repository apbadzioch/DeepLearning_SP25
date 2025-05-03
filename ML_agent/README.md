# Process Automation Agent - ITAI 2376 Final Project
## Project Overview
This AI agent is designed to streamline repetitive administrative tasks. It autonomously handles complex workfolws such as scheduling meetings, sending emails, and managing follow-ups. The goal is to increase efficiency and reduce human workload through intelligent task planning, execution, and feedback-based improvement.

**Project Type:** Process Automation Agent
**Course:** ITAI 2376 - Deep Learning
**Semester:** Spring 2025
**Team Name:** Epoch Explorers
**Team Members:**
- Andrew Badzioch
- Naomi Beruman
- Eduardo Cabrera-lopez
- Monica Joya
---
## Features

- Task decomposition and dynamic prioritization
- Multi-step execution with error handling
- Real-time progress tracking and user interaction
- Simulated integration with external tools:
    - 'calendar_tool.py' for event scheduling
    - 'reminder_tool.py' for message scheduling
- Reinforement Learning simulation via 'FeedbackManager'
- Safety measures: input validation, fallbacks, boundry checks

---
## How to Run
1. Upload all project files into Azure AI Studio or run locally in a Python 3.10+ environment
2. (Optional) Create a virtual environment and activate it:
'''bash
python -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows
'''
3. Install dependencies (minimal):
'''
pip install -r requirements.txt
'''
4. Run the main assistant:
'''
python core.py
'''
