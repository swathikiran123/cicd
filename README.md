# 🚀 Real-World Software Pipeline Simulation using Python Abstraction
This project simulates a real-world development workflow commonly used by software, data engineering, and machine learning teams.

🎯 Goal:
To understand how professional teams structure code, maintain abstraction, and integrate versioning and CI/CD practices using GitHub.

# 📌 Project Workflow

| Role                   | Responsibility                                                       | File               |
| ---------------------- | -------------------------------------------------------------------- | ------------------ |
| 👨‍💻 Senior Developer | Designs the base structure using abstract classes                    | `Version1.py`      |
| 👩‍💻 Junior Developer | Implements actual logic by extending the base structure              | `Version2.py`      |
| 🧑‍🚀 End User         | Runs the complete pipeline via a simple command-line interface (CLI) | `main_version2.py` |



# 🔁 Versioned Development Flow
Version	Role	Description
V1	Senior Dev	Abstract base structure
V2	Junior Dev	Implements core logic based on V1
V3	Senior Dev	Adds new abstract methods for extended functionality
V4	Junior Dev	Implements new features introduced in V3

# 🛠️ Technologies & Concepts Used
Python OOP — Abstract Base Classes (abc)

Modular Coding — Clean and maintainable codebase

CLI Tooling — User-friendly interface using argparse

Version Control — Git + GitHub workflow simulation

YOLOv8 Integration — Basic object detection example

Abstraction-Driven Design — Separation of roles and logic

# ⚙️ How to Run This Project
# Clone the repository
git clone https://github.com/swathikiran123/cicd.git
cd your-repo-name

# Run the pipeline
python main_version2.py --image_path="sample.jpg" --model_path="yolov8n.pt"


✅ Make sure to install required dependencies:


## pip install -r requirements.txt

# 🧠 Learning Outcomes

Understand the power of abstraction in large-scale projects

Learn how teams collaborate and divide responsibilities

Gain experience with versioned code development

Practice maintainable, integration-ready Python programming

Explore how GitHub workflows mimic real CI/CD pipelines
