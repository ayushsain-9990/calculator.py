import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except Exception:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found!")
        return
    print("\n📋 --- YOUR TO-DO LIST ---")
    for idx, task in enumerate(tasks, 1):
        status = "✅ Done" if task["completed"] else "❌ Pending"
        print(f"{idx}. {task['title']} [{status}]")

def main():
    tasks = load_tasks()
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks\n2. Add Task\n3. Mark Task as Done\n4. Delete Task\n5. Exit")
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter task name: ").strip()
            if title:
                tasks.append({"title": title, "completed": False})
                save_tasks(tasks)
                print("✅ Task added!")
        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                try:
                    num = int(input("Enter task number to mark as done: "))
                    if 1 <= num <= len(tasks):
                        tasks[num - 1]["completed"] = True
                        save_tasks(tasks)
                        print("🎉 Task marked as completed!")
                    else:
                        print("❌ Invalid task number.")
                except ValueError:
                    print("❌ Please enter a valid number.")
        elif choice == "4":
            show_tasks(tasks)
            if tasks:
                try:
                    num = int(input("Enter task number to delete: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        save_tasks(tasks)
                        print(f"🗑️ Removed: {removed['title']}")
                    else:
                        print("❌ Invalid task number.")
                except ValueError:
                    print("❌ Please enter a valid number.")
        elif choice == "5":
            print("👋 Exiting To-Do List Application.")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()