print("Welcome to TO-DO APP".center(50,'-'))
print("")
todo_arr=[]


def to_do_func():
    print("Enter The Task Your Required")
    print("")
    print("1: Add Task")
    print("2: Remove Task")
    print("3: View Task")
    print("4: Quit")
    print("")
    get_user_inp=int(input("Enter Your Requirement: "))
    if get_user_inp==1:
        def addtask():
            global todo_arr
            get_task_to_add=input("Enter Tak to add: ")
            todo_arr.append(get_task_to_add)
            print("Task Added Successfully")
            get_again_add=input("Want to add more(y,n):").lower().strip()
            if get_again_add=='y':
                return addtask()
            else:
                return to_do_func()
        addtask()
    elif get_user_inp==2:
        def remove_task():
            global todo_arr
            for index,task in enumerate(todo_arr):
                print(f"{index}: {task}")
            get_rem_inp=int(input("Enter The task Number to remove: "))
            del todo_arr[get_rem_inp]
            print("Task has Been Removed")
            for index,task in enumerate(todo_arr):
                print(f"{index}: {task}")
            

        remove_task()
        print("")
        return to_do_func()
    elif get_user_inp==3:
        global todo_arr
        for index,task in enumerate(todo_arr):
                print(f"{index}: {task}")
        print("")
        print("All Task Were Listed")
        return to_do_func()

    elif get_user_inp==4:
        print("Thank You") 
    else:
        print("Please Enter the Valid Input")
        return to_do_func()
to_do_func()
