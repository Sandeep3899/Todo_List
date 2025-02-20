# 📝 To-Do List App (with File Handling)

## 📌 Overview
This is a simple **To-Do List** application written in Python. It allows users to **add, view, and remove tasks**, while persisting tasks in a file (`tasks.txt`). This ensures that tasks are saved even after the program is closed.

## 🎯 Features
✅ Add tasks to the list  
✅ View all saved tasks  
✅ Remove completed tasks  
✅ Tasks are saved automatically in `tasks.txt`  
✅ Uses Python's **file handling** for persistent storage  

## 🛠 Technologies Used
- Python 3.x
- File Handling (`open()`, `read()`, `write()`)
- Error Handling (`try-except`)
- Basic CLI (Command Line Interface)

## 🚀 How to Run the Project
### **1️⃣ Clone the Repository**

git clone https://github.com/yourusername/todo-list-python.git
cd todo-list-python

2️⃣ Run the Python Script
python todo_list.py

📌 How It Works
On startup, the program reads tasks from tasks.txt (if it exists).
Users can add, view, and remove tasks.
Every change is automatically saved to the file.

🏗️ Code Structure

📂 todo-list-python
 ┣ 📜 todo_list.py    # Main Python script
 ┣ 📜 tasks.txt       # Stores saved tasks
 ┗ 📜 README.md       # Project documentation

📝 Example Usage
To-Do List Menu:
1. Add Task
2. View Tasks
3. Remove Task
4. Exit

Choose an option (1-4): 1
Enter a new task: Finish Python Project
✅ Task added: Finish Python Project

Choose an option (1-4): 2
Your Tasks:
1. Finish Python Project
📌 Future Enhancements
🔹 Add a GUI version using Tkinter
🔹 Implement task priorities (High, Medium, Low)
🔹 Use database storage instead of a text file

📜 License
This project is open-source
