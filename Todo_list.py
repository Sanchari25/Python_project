def ToDo_list():
    print("\n---ToDo_list menu---")
    print("1. View list")
    print("2. Add Work")
    print("3. Update Work")
    print("4. Delete Work")
    print("5. Exit")

work_list=[]

while True:
    ToDo_list()
    choice= input("Enter your choice (1-5):")

    if choice=='1':
        if work_list:
            print("\n Your work list:")
            for idx, work in enumerate(work_list, start=1):
                print(f"{idx}.{work}")
        else:
            print("\n Your list is empty.")
    elif choice=='2':
        new_work= input("Enter the work you want to add:")
        work_list.append(new_work)
        print("Work added sucessfully")
    
    elif choice=='3':
        if not work_list:
            print("The list is empty, nothing to update")
        else:
            for idx, work in enumerate(work_list, start=1):
                 print(f"{idx}.{work}")
            try:
                index= int(input("Enter the number of the work you want to update:"))-1
                if 0<= index<len(work_list):
                    update_work= input("Enter the new work:")
                    work_list[index]= update_work
                    print("Work updated sucessfully")
                else:
                    print("Invalid index")
            except ValueError:
                print("Plese enter a valid number")
    
    elif choice=='4':
        if not work_list:
            print("The list is empty, nothing to remove")
        else:
            for idx, work in enumerate(work_list, start=1):
                 print(f"{idx}.{work}")
            try:
                index= int(input("Enter the number of the work you want to delete:"))-1
                if 0<= index<len(work_list):
                    removed= work_list.pop(index)
                    print(f"'{removed}'Removed sucessfully")
                else:
                    print("Invalid index")
            except ValueError:
                print("Plese enter a valid number")

    elif choice=='5':
        print("Exit")
        break
    else:
        print("Invalid choice, please enter a valid number from 1 to 5.")


        

                





