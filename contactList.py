contact_list = {}
while True:
    print("\nOptions:")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Edit contacts")
    print("4. Delete contacts")
    print("5. Exit")
    choice = input("Choose an option (1/2/3): ")
    if choice == '1':
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
            print("\nContact List:")
            print(contact_list)
    elif choice == '3':
        name = input("Enter the name you want to edit: ")
        if name in contact_list:
            print("Editing contact...")
            u_phone = input("Enter new Phone Number (leave blank to keep current): ")
            u_age = input("Enter new Age (leave blank to keep current): ")
            u_email = input("Enter new Email Address (leave blank to keep current): ")
        contact_list[name] = {'phone' : u_phone , 'age' : u_age , 'email' : u_email}
        print("Contact edited successfully!")
            
    elif choice == '5':
        print("Exiting the program.")
        break

    else:   
        print("Invalid choice. Please try again.")
