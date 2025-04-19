import datetime

class Task:
    def __init__(self, title, deadline, priority):
        self.title = title
        self.deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d")
        self.priority = priority

    def __str__(self):
        return f"{self.title} (Due: {self.deadline.date()}, Priority: {self.priority})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, deadline, priority):
        task = Task(title, deadline, priority)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("Your Tasks:")
        for idx, task in enumerate(sorted(self.tasks, key=lambda t: (t.deadline, t.priority)), 1):
            print(f"{idx}. {task}")

    def remove_task(self, index):
        try:
            removed_task = self.tasks.pop(index - 1)
            print(f"Task '{removed_task.title}' removed successfully!")
        except IndexError:
            print("Invalid task number.")

def main():
    manager = TaskManager()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            priority = int(input("Enter priority (1-5): "))
            manager.add_task(title, deadline, priority)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.view_tasks()
            index = int(input("Enter task number to remove: "))
            manager.remove_task(index)
        elif choice == "4":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()