#project TASK_OF_THE_DAY list
import os

TODO_FILE = "todo_list.txt"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return [task.strip() for task in f.readlines()]
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(f"{task}\n")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")
    save_tasks(tasks)

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def mark_task_complete(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to mark as complete: "))
    if 1 <= task_num <= len(tasks):
        completed_task = tasks.pop(task_num - 1)
        print(f"Task '{completed_task}' completed.")
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to delete: "))
    if 1 <= task_num <= len(tasks):
        deleted_task = tasks.pop(task_num - 1)
        print(f"Task '{deleted_task}' deleted.")
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task Complete\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
