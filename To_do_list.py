#file handling
import os

TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from a file into a list"""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    return []

def save_tasks():
    """Save the current task list to a file"""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    """Display menu options"""
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    """Function to add a task and save it to file"""
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks()  # Save updated tasks to file
    print(f"✅ Task added: {task}")

def view_tasks():
    """Function to display all tasks"""
    if not tasks:
        print("📌 No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task():
    """Function to remove a task and update file"""
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                save_tasks()  # Save updated list after deletion
                print(f"❌ Removed Task: {removed}")
            else:
                print("⚠ Invalid task number.")
        except ValueError:
            print("⚠ Please enter a valid number.")

# Load existing tasks when the program starts
tasks = load_tasks()

while True:
    show_menu()
    choice = input("\nChoose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("🚀 Exiting To-Do List. Have a great day!")
        break
    else:
        print("⚠ Invalid choice. Please select a valid option.")
