**ITAI 2376:** Deep Learning  
**Final Report:** Virtual Administrative Assistant AI Agent  
**Team Name:** Epoch Explorers  
**Team Members:** Naomi Berumen, Monica Joya, Eduardo Cabrera, Andrew Badzioch

### **Project Overview**

Our capstone project for ITAI 2376 was to design and implement an AI agent system that could automate multi-step administrative processes using language-based reasoning and decision-making. We chose Option 2: Process Automation Agent and created a Virtual Administrative Assistant that performs tasks like scheduling meetings and sending emails in response to natural language user input. 

Output creation and logging are done using OpenAI's GPT model for reasoning and planning, n8n for process execution, and external applications including Google Calendar, Gmail, and Google Sheets. The agent also includes built-in error handling and reinforcement learning elements via outcome tracking. This project let our team work together in a cloud-based development environment applying course ideas in a practical automation context.

### **Agent Architecture**

Our agent follows a modular structure with the following components:

* Input Processing: The agent receives natural language messages via an n8n webhook trigger.  
* Reasoning Component: OpenAI's GPT model is used to determine the user's intent and decompose high-level instructions (e.g., "schedule a meeting") into an action, message, date, and time.  
* Conditional Logic: A combination of If and Switch nodes in n8n determine whether to create a calendar event, send an email, or log an unrecognized action.  
* Output Execution: The agent takes action by either creating a Google Calendar event or sending an email via Gmail.  
* Confirmation: After completing a task, a confirmation message is sent back to the user.

### **Tool Integration**

We successfully integrated the following tools:

* Google Calendar API: Used to create meeting events based on the extracted date, time, and participant details.  
* Gmail API: Used to send emails with dynamically generated content.  
* Google Sheets: Logs unrecognized or unhandled requests with details like the action, timestamp, and user input.

Our agent follows every tool integration guideline. Every tool interaction has built-in error management including fallbacks should API requests fail. For instance, the request is recorded and the user informed if a calendar creation fails because of lacking data. Before proceeding to the next execution stage, every tool output is checked. The GPT model's structured answer lets the system decide which tool—Calendar or Gmail—should be engaged, so tool use is also context-aware.

### **Reinforcement Learning Elements**

While we did not implement traditional reinforcement learning algorithms, we incorporated RL principles by:

* Logging each task with a status field (e.g., success or unhandled)  
* Tracking task timestamps  
* Differentiating fallback paths for unknown actions  
* Allowing performance review over time using the Google Sheets log

This gives the agent a foundational structure for future policy improvement and learning based on outcomes.

### **Safety and Security Features**

Our agent includes multiple safety mechanisms:

* Input Validation: Uses conditional nodes to detect and route unknown or malformed inputs.  
* Defined Boundaries: Only schedule\_meeting and send\_email actions are allowed. All other inputs are logged but not executed.  
* Fallback Strategy: If the action is not recognized, the input is logged to Google Sheets, and a fallback confirmation message is sent.  
* Transparency: The confirmation message clearly states whether a task was performed or if the input could not be handled.

All input is checked at the webhook level; only acknowledged intents are forwarded forward. To reduce risk, the system is purposefully limited to two activities (schedule\_meeting, send\_email). Any invalid or unsupported inputs are sent to the fallback log and handled safely for the user. This guarantees the agent stays explainable and open in behavior and stops unintentional execution.

### **Development Environment**

We used n8n Cloud as our primary development platform, allowing us to visually design, test, and deploy the workflow without requiring a local server setup. Additionally, we used Google Colab for planning and prototyping logic.

### **Limitations and Future Work**

While the agent performs its core functions effectively, we identified areas for future improvement:

* Adding natural language reminders and rescheduling logic  
* Expanding action recognition using few-shot learning in GPT  
* Adding user authentication to restrict access  
* Logging successful tasks to Google Sheets for full analytics

Future versions could include these enhancements or they could be included to a more comprehensive process automation system.

### **Conclusion**

The Virtual Admin Assistant demonstrates a functional, modular AI agent capable of interpreting user instructions, performing multi-step tasks, and adapting to input conditions. Our project reflects a practical application of language-based planning, tool integration, and outcome tracking in real-world automation scenarios. We are proud of the system we've built and look forward to expanding it further. Modular agent architecture, reasoning using LLMs, secure tool integration, and policy development through result tracking among others fit this project with fundamental learning goals from ITAI 2376\. Even without significant infrastructure needs, we think the system shows how cloud-native tools and smart integration of language models may be used to construct useful AI agents.
