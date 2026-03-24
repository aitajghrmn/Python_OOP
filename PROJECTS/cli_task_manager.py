def show_menu():
    print("\n--- TASK MANAGER ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")


def add_task(tasks):
    task_name = input("Enter task name: ").strip()

    if task_name == "":
        print("Task name cannot be empty.")
        return

    tasks.append(task_name)
    print(f"Task '{task_name}' added successfully.")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
        return

    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def delete_task(tasks):
    if len(tasks) == 0:
        print("No tasks to delete.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' deleted successfully.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


main()
