choice = ""
taskList = []
while choice != "exit":
    choice = input(
        "Press : \n 1: Add task \n 2: Show Task \n 3: Complete Task \n 4: summary \nexit: Exit \n"
    )
    if choice == "1":
        taskname = input("Enter task : ")
        d = {taskname: False}
        taskList.append(d)
        print("Task Added SuccessFully \n")
    elif choice == "2":
        print(taskList)
    elif choice == "3":
        t = input("Enter task to mark as complete")
        if {t: False} in taskList:
            i = taskList.index({t: False})
            taskList[i] = {t: True}
            print("task ", t, " is completed")
        else:
            print("item not present")
    elif choice == "4":
        total = len(taskList)
        completed = 0
        for t in taskList:
            for v in t.values():
                if v:
                    completed = completed + 1
        pending = total - completed
        print(
            f"Total Task : {total}  \n completed task :  {completed}   , pending :{pending}"
        )
