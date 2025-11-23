# 🧠 SynthMind 

**The Transparent AI Co-Designer.**
*Turn ideas into working prototypes while watching the AI "think."*

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-red)
![Gemini AI](https://img.shields.io/badge/Powered%20By-Gemini%202.5%20Pro-4285F4)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Overview

**SynthMind** is not just a code generator; it is an **Agentic Workflow System** designed to solve the "Black Box" problem in AI development.

Standard AI tools (like ChatGPT) often generate buggy code because they try to solve complex problems in a single shot. SynthMind solves this by breaking the creation process into three distinct, self-correcting roles: **Designer**, **Coder**, and **Critic**.

By forcing the AI to **plan** before it **codes** and **critique** its own work before it **delivers**, SynthMind significantly reduces logic errors and hallucinations.

---

## ⚡ Why SynthMind?

Most developers spend hours debugging AI-generated code. SynthMind cuts that time by automating the "Senior Developer" review process.

| Feature | 🔴 Standard AI (ChatGPT) | 🟢 SynthMind Ω |
| :--- | :--- | :--- |
| **Workflow** | Linear (Input → Output) | **Cyclical** (Plan → Code → Critique) |
| **Reliability** | Prone to "Self-Correction Blind Spots" | **High** (The Critic Agent catches errors early) |
| **Transparency** | "Black Box" (No reasoning shown) | **White Box** (Explains *why* decisions were made) |

---

## 🛠️ The Architecture

SynthMind uses a **Multi-Agent System** powered by Google's Gemini 2.5 Pro:

1.  **🎨 The Designer Agent**
    * **Role:** Interprets the user's one-sentence goal.
    * **Output:** Creates a high-level system architecture and data flow diagram.
    * *Why?* Prevents "spaghetti code" by planning structure first.

2.  **💻 The Coder Agent**
    * **Role:** Translates the Designer's blueprint into functional Python/Pseudocode.
    * **Output:** Skeleton code with comments explaining the logic.
    * *Why?* Focuses purely on logic implementation without distraction.

3.  **🧐 The Critic Agent**
    * **Role:** Reviews both the Design and the Code.
    * **Output:** Identifies edge cases, logic flaws, and suggests improvements.
    * *Why?* Breaks the "hallucination loop" by providing an external review.

---

## 📦 Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/SynthMind.git](https://github.com/YOUR_USERNAME/SynthMind.git)
cd SynthMind
2. Create a Virtual Environment (Recommended)
Windows (PowerShell):

PowerShell

python -m venv venv
.\venv\Scripts\Activate
Mac/Linux (Bash):

Bash

python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash

pip install -r requirements.txt
🔑 Configuration
You need a Google Gemini API Key to run the AI agents.

Get a free key here: Google AI Studio

Launch the app (see below).

Paste your API key into the Sidebar when the app opens.

(Note: The app does not store your API key permanently for security reasons.)

▶️ Usage
Run the Streamlit application:

Bash

streamlit run app.py
A browser window will open automatically at http://localhost:8501.

Step 1: Paste your Gemini API Key in the sidebar.

Step 2: Enter your idea in the text box (e.g., "A fitness tracker that adjusts goals based on my sleep data").

Step 3: Click "Initialize Co-Design Process".

Step 4: Explore the Designer, Coder, and Critic tabs to see how the AI built your project.



🔮 Future Roadmap
[ ] Persistent Memory: Add SQLite database to save user projects and "Blueprints."
[ ] Auto-Fix Loop: Allow the "Critic" to automatically send instructions back to the "Coder" to fix bugs without human intervention.
[ ] File Export: Button to download the generated code as a .py or .zip file.



🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE for more information.

Built with ❤️ by [Your Name] Powered by Streamlit & Google Gemini
