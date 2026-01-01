#load existing items
# 1. creating a new item
# 2. List items
# 3. Mark items as complete
#4. save items
#add on delete a task

import  json

file_name= "../Files/to_do_list.json"

def load_task():
    try:
        with open(file_name,"r") as json_file:
            return json.load(json_file)
    except:
        return {"tasks" : []}

def save_task(task):
    try:
        with open(file_name, "w") as json_file:
            return json.dump(task,json_file)
    except:
        print("Error saving task")

def view_task(task):
    task_list = task["tasks"]
    if len(task_list) == 0:
        print("No tasks")
    else:
        print("\n Your To Do List:")
        for idx, task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{idx + 1}. {task['description']} | {status}")


def create_task(task):
    description = input("Enter the task description: ").strip()
    if description:
        task["tasks"].append({"description": description, "complete": False})
        save_task(task)
        print("Task saved")
    else:
        print("Task description cannot be empty")


def mark_task_complete(task):
    view_task(task)
    try:
        task_num = int(input ("Enter task number to mark as complete: ").strip())
        if 1 <= task_num <= len(task):
            task["tasks"][task_num-1]["complete"] = True
            save_task(task)
            print("Task marked as complete")
        else:
            print("Invalid task number")
    except:
        print("Invalid task number")

def del_task(task):
    task_list = task["tasks"]
    if len(task_list) == 0:
        print("No tasks")
    else:
        for i, task in enumerate(task_list):
            print(f"{i+1}. {task['description']}")
        try:
            choice = int(input("Enter task number to delete: "))
            if 1 <= choice <= len(task):
                deleted = task_list.pop(choice - 1)
                save_task(task_list)
                print(f"Deleted task: {deleted['description']}")
            else:
                print("Invalid task number")
        except:
            print("Please enter a valid number")





def main():
    task = load_task()

    while True:
        print("\n TO-DO List Manager")
        print("1. View task")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            view_task(task)
        elif choice == "2":
            create_task(task)
        elif choice == "3":
            mark_task_complete(task)
        elif choice == "4":
            del_task(task)
        elif choice == "5":
            print("Thank you for playing")
            break
        else:
            print("Invalid choice")


main()