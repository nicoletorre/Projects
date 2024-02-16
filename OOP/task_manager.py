import json
import os
from datetime import datetime, date

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        elif isinstance(obj, (Task, ErrorTask)):
            return obj.__dict__
        return super().default(obj)

class TaskEntry:
    def __init__(self, title, description, deadline=None, completed=False):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        deadline_str = f"Deadline: {self.deadline}" if self.deadline else "No Deadline"
        return f"{self.title}\nDescription: {self.description}\n{deadline_str}\nStatus: {status}\n"

class Task(TaskEntry):
    def __init__(self, title, description, deadline=None, completed=False, priority=None):
        super().__init__(title, description, deadline, completed)
        self.priority = priority

    def __str__(self):
        task_entry_str = super().__str__()

        if self.priority:
            priority_str = f"Priority: {self.priority}"
            return f"{task_entry_str}{priority_str}\n"
        else:
            return task_entry_str


class ErrorTask(TaskEntry):
    def __init__(self, error_message):
        self.error_message = error_message
        super().__init__("N/A", "N/A", None, False)

    def __str__(self):
        return f"Error: {self.error_message}"

class TaskManager:
    def __init__(self, filename='task_manager.json'):
        self.filename = filename
        self.tasks = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.tasks = [Task(**task_data) if 'error_message' not in task_data else ErrorTask(task_data['error_message']) for task_data in data]
        except (json.JSONDecodeError, IOError, FileNotFoundError):
            print("Error loading data from JSON file.")

    def save_data(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.tasks, file, indent=2, cls=DateTimeEncoder)
            print("Data saved to JSON file.")
        except ValueError:
            print("Error saving data to JSON file.")

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print('No tasks at the moment.')
        else:
            print('Tasks:')
            for task in self.tasks:
                print(task)

    def edit_task(self, index, new_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = new_task
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            task_to_delete = self.tasks[index - 1]
            print("Are you sure you want to delete the following task?")
            print(task_to_delete)
            confirmation = input("Type 'yes' to confirm or any other input to cancel: ")
            if confirmation.lower() == 'yes':
                del self.tasks[index - 1]
                self.save_data()
                print("Task deleted successfully.")
            else:
                print("Task deletion canceled.")
        else:
            print("Invalid task index.")

    def complete_task(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].completed = True
        else:
            print("Invalid task index.")

    def Menu(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Edit Task")
            print("4. Delete Task")
            print("5. Complete Task")
            print("6. Save Data to JSON")
            print("7. Load Data from JSON")
            print("8. Exit")
            print()

            choice = input("Enter your choice (1-8): ")

            if choice == '1':
                try:
                    title = input("Enter task title: ")
                    description = input("Enter task description: ")
                    deadline_str = input("Enter task deadline (optional, format: YYYY-MM-DD): ")
                    priority_input = input('Priority: ')
                    
                    if priority_input.lower() == 'yes':
                        priority = input('Enter task priority: ')
                    else:
                        priority = None
                    
                    if deadline_str:
                        deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
                    else:
                        deadline = None

                    task = Task(title, description, deadline, priority=priority)
                    self.add_task(task)
                except ValueError:
                    print("Invalid deadline format. Please use the format: YYYY-MM-DD.")
                    
            elif choice == '2':
                self.view_tasks()
                
            elif choice == '3':
                index = int(input("Enter index of task to edit: "))
                try:
                    title = input("Enter new task title: ")
                    description = input("Enter new task description: ")
                    deadline_str = input("Enter new task deadline (optional, format: YYYY-MM-DD): ")

                    if deadline_str:
                        deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
                    else:
                        deadline = None
                    new_task = Task(title, description, deadline)
                    self.edit_task(index, new_task)
                    
                except ValueError:
                    print("Invalid deadline format. Please use the format: YYYY-MM-DD.")
                    
            elif choice == '4':
                index = int(input("Enter index of task to delete: "))
                self.delete_task(index)
                print()
                
            elif choice == '5':
                index = int(input("Enter index of task to mark as completed: "))
                self.complete_task(index)
                
            elif choice == '6':
                self.save_data()
                print("Data saved manually.")
                
            elif choice == '7':
                self.load_data()
                
            elif choice == '8':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.Menu()
