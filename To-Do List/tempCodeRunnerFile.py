
tasks = []


def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

def view_tasks():
    if len(tasks) == 0:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("\nEnter the task you want to add: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")

def remove_task():
    view_tasks()  
    try:
        task_number = int(input("\nEnter the task number you want to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"'{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Please enter a valid task number.")

def to_do_list_app():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1/2/3/4): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

to_do_list_app()

