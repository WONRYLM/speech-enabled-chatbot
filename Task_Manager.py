# Simple Task Manager using Python lists

task_list = []
while True:
    print("\nTask Manager","1. Add Task","2. View Tasks","3. Remove Task","4. Mark Task as Done","5. Exit")
    
    option = 0
    x = (input ("Enter your option (1-5): "))  #check if the list is empty or not
    if not x.isdigit():
        print("Invalid option,enter a number between 1 and 5")
        continue
    option = int(x)
    if option < 1 or option > 5:
        print("Input should be between 1 and 5!")
        continue
    if option == 1:
        task = input("Enter your Task : ")
        task_list.append(task)
        print("Task added successfully")
    elif option == 2:
        if not task_list:
            print("No tasks available")
        for x in task_list:
            print("Tasks:", x)
    elif option == 3:  
        if not task_list:
            print("No tasks available")
        else:    
            for x in task_list:
                print("Tasks:", x)
            task = input("Enter the task you want to remove: ")
            task_list.remove(task)
            print("Task removed successfully")
    elif option == 4:
        for i in range(len(task_list)):
            if task_list[i] == task:
                task_list[i] = "Done"
        if not task_list:
            print("No tasks to mark as done")
    elif option == 5:
        print("Exiting Task Manager")
        break
        



# if choice == '1':
#     task = input("Enter the task to add: ")
#     task_list.append({"task": task, "done": False})
#     print(f"Task '{task}' added successfully!")
    
# print(task_list)
# del task_list[0]
# print(task_list)