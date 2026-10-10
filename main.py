import os

FILE_NAME = "tasks.txt"

def show_task():

    if not os.path.exists(FILE_NAME):
        print("\n No task found yet! try adding task first")
        return False

    with open(FILE_NAME,"r") as f:
        tasks= f.readlines()

        if not tasks:
            print("\n your list is empty")
            return False
        
        print("\n--- YOUR TO-DO LIST : ---\n")
        for index,task in enumerate(tasks,start =1):
            print(f"{index}.{task.strip()}")

        print("--------------------\n")
        return True

def add_task():
    task = input("enter the task you want to add:")

    with open(FILE_NAME,"a") as f:
        f.write(task + "\n")
    print("Task added successfully! \n")

def delete_task():
    has_task = show_task()
    if not has_task:
        return

    try:
        choice = int(input("Enter task number to delete"))

        with open(FILE_NAME,"r") as f:
            tasks = f.readlines()

        if 1<= choice <=len(tasks):
            removed_task = tasks.pop(choice-1)

            with open(FILE_NAME,"w") as f:
                f.writelines(tasks)

            print(f"Deleted Task: '{removed_task.strip()}' sucessfully! \n")
        else:
            print("Invalid task number! Please enter a valid number from the list. \n")
    except ValueError:
        print("please enter a valid numeric number!\n")


while True:
    print("\n"+"="*20)
    print("==== To-Do list ====")
    print("1. View Task")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    print("="*20)


    choice = input("Choose an option (1-4): ") 
    if choice=="1":
        show_task()
    elif choice =="2":
        add_task()
    elif choice =="3":
        delete_task()
    elif choice =="4":
        print("Exiting.... Have a Productive day!")
        break
    else:
        print("Invalid Choice, please enter 1,2,3 or 4 \n")
