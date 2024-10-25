contact_list = {}
while True:
    print("\n***Main Menu***\n")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Edit contacts")
    print("4. Delete contacts")
    print("5. Search Contacts")
    print("6. Sort Your Contacts")
    print("7. Exit")
    choice = input("Enter  your choice: ")
    print("\n")

    if choice == '1':
        name = input("Enter Name: ")
        if name in contact_list:
            print("Contact already exists")
            print("Enter Unique Name: ")
            name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        age = input("Enter Age: ")
        email = input("Enter Email Address: ")
        contact_list[name] = {'phone': phone, 'age': age, 'email': email}
        print("Contact added successfully!") 
    elif choice == '2':
        if not contact_list:
            print("No contacts available.")
        else:
            for name, details in contact_list.items():
                print(f" Name: {name}\n Phone Number: {details['phone']}\n Age:  {details['age']}\n Email-> {details['email']}")
    elif choice == '3':
        name = input("Enter the name you want to edit: ")
        if name in contact_list:
            print("Editing contact...")
            u_phone = input("Enter new Phone Number (leave blank to keep current): ")
            u_age = input("Enter new Age (leave blank to keep current): ")
            u_email = input("Enter new Email Address (leave blank to keep current): ")
        contact_list[name] = {'phone' : u_phone , 'age' : u_age , 'email' : u_email}
        print("Contact edited successfully!")
    elif choice == '4':
        name = input("Enter the name you want to delete: ")
        if name in contact_list:
            del contact_list[name]
            print(f"{name} Deleted sucessfuly!")
        else:
            print(f"{name} not found!")
    elif choice == '5':
        name = input("Enter the name you want to search: ")
        if name in contact_list:
            print(f"Name: {name}")
            print(f"Phone Number: {contact_list[name]['phone']}")
            print("Exiting the program...")
        else:
            print(f"{name} not found!")
    elif choice == '6':
        print("Sorting contacts...")
        sorted_dict = dict(sorted(contact_list.items()))
        print(sorted_dict ,"\n")
    elif choice == '7':
        print("Exiting the program.")
        break

    else:   
        print("Invalid choice. Please try again.")
