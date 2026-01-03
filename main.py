def show_menu():
    print("\n📌 SMART TASK ORGANIZER")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    task_name = input("Enter task name: ")
    priority = input("Enter priority (High/Medium/Low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    task = f"{task_name} | {priority} | {due_date} | Pending\n"

    with open("tasks.txt", "a") as file:
        file.write(task)

    print("✅ Task added successfully!")


def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("📭 No tasks found.")
            return

        print("\n📋 Your Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.strip()}")

    except FileNotFoundError:
        print("❌ tasks.txt file not found.")


def mark_task_completed():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("📭 No tasks to update.")
            return

        view_tasks()
        task_number = int(input("Enter task number to mark as completed: "))

        if task_number < 1 or task_number > len(tasks):
            print("❌ Invalid task number.")
            return

        parts = tasks[task_number - 1].strip().split(" | ")
        parts[-1] = "Completed"
        tasks[task_number - 1] = " | ".join(parts) + "\n"

        with open("tasks.txt", "w") as file:
            file.writelines(tasks)

        print("✅ Task marked as completed!")

    except ValueError:
        print("❌ Please enter a valid number.")
    except FileNotFoundError:
        print("❌ tasks.txt file not found.")


def delete_task():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("📭 No tasks to delete.")
            return

        view_tasks()
        task_number = int(input("Enter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("❌ Invalid task number.")
            return

        deleted_task = tasks.pop(task_number - 1)

        with open("tasks.txt", "w") as file:
            file.writelines(tasks)

        print(f"🗑️ Deleted: {deleted_task.strip()}")

    except ValueError:
        print("❌ Please enter a valid number.")
    except FileNotFoundError:
        print("❌ tasks.txt file not found.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("🎉 Project Completed. Bye 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")


main()




