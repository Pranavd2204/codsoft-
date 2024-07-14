import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("To-Do List Application")
    print("-----x----x----x------")
    print("1.Add a task")
    print("2.View all tasks")
    print("3.Mark a task as done")
    print("4.Delete a task")
    print("5.Exit")
    print("-----x-----x----x-----")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}. {task['task']} [{status}]")

def mark_task_done(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["done"] = True
        print(f"Task '{tasks[task_num]['task']}' marked as done.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        removed_task = tasks.pop(task_num)
        print(f"Task '{removed_task['task']}' deleted.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        clear_screen()
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
            input("Press Enter to continue")
        elif choice == '3':
            mark_task_done(tasks)
            input("Press Enter to continue")
        elif choice == '4':
            delete_task(tasks)
            input("Press Enter to continue")
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")
            input("Press Enter to continue")

if __name__ == "__main__":
    main()
