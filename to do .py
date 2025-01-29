# To-Do List Application in Python

class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"Task '{task}' added.")

    def remove_task(self, task_index):
        try:
            task = self.tasks.pop(task_index)
            print(f"Task '{task['task']}' removed.")
        except IndexError:
            print("Invalid task index.")

    def mark_done(self, task_index):
        try:
            self.tasks[task_index]["done"] = True
            print(f"Task '{self.tasks[task_index]['task']}' marked as done.")
        except IndexError:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            for index, task in enumerate(self.tasks):
                status = "Done" if task["done"] else "Pending"
                print(f"{index + 1}. {task['task']} [{status}]")

def main():
    app = TodoApp()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Done")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            app.add_task(task)
        elif choice == '2':
            app.view_tasks()
            try:
                task_index = int(input("Enter the task number to remove: ")) - 1
                app.remove_task(task_index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            app.view_tasks()
            try:
                task_index = int(input("Enter the task number to mark as done: ")) - 1
                app.mark_done(task_index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '4':
            app.view_tasks()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
