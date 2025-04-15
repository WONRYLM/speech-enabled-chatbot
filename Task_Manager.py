# Simple Task Manager using Python lists

task_list = []
# Starting the while loop
while True:
    print("\nTask Manager","1. Add Task","2. View Tasks","3. Remove Task","4. Mark Task as Done","5. Exit")
    
    option = 0
    x = (input ("Enter your option (1-5): "))  
    if not x.isdigit():                         #TO  ensure that the value entered is a digit
        print("Invalid option,enter a number between 1 and 5")
        continue                                #To ensure the program continues running 
    option = int(x)
    if option < 1 or option > 5:                #To ensure that the value entered is within the range
        print("Input should be between 1 and 5!")
        continue                                #To ensure the program continues running
    # Adding a task
    if option == 1:
        task = input("Enter your Task : ")
        task_list.append(task)
        print("Task added successfully")
    # Viewing tasks    
    elif option == 2:
        if not task_list:                       #Checking if list is empty or not
            print("No tasks available")
        for x in task_list:
            print("Tasks:", x)
    # Removing tasks        
    elif option == 3:  
        if not task_list:                       #Ensures information is relayed back to the user
            print("No tasks available")
        else:    
            for x in task_list:
                print("Tasks:", x)
            task = input("Enter the task you want to remove: ")
            task_list.remove(task)
            print("Task removed successfully")
    # Marking tasks as done
    elif option == 4:
        for i in range(len(task_list)):
            if task_list[i] == task:
                task_list[i] = "Done"
        if not task_list:
            print("No tasks to mark as done")
    # To exit the task manager        
    elif option == 5:
        print("Exiting Task Manager")
    # Breaking the loop to exit the task manager
        break
        



# if choice == '1':
#     task = input("Enter the task to add: ")
#     task_list.append({"task": task, "done": False})
#     print(f"Task '{task}' added successfully!")
    
# print(task_list)
# del task_list[0]
# print(task_list)