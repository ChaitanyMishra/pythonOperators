import random
Passlist =[]
while True:
    print("NOTE* size of the password must be 'INTEGER DIGIT' or gretar then '0'!")
    size = int(input("Enter the size of your password! "))
    if size>0:
        pas=""
        backend = "~`@#$%^&*()_-=+QWERTYUIOPLKJHGFDSAZXCVBNMmnbvcxzasdfghjklpoiuytrewq[]{}|;:',<.>?"
        for i in range(1 ,size+1):
            pas+=random.choice(backend)
        print(f"Genrated password --> {pas} ")
        Passlist.append(pas)
        print("Press any key to exit! or")
        ask =int(input("change password? press '1'  to create new password! "))
        if ask != 1:
            print(f"thankyou for using strong password genratior!\nExiting... ")
            break
    else:
        print("Invalid input!")
print(f"Your previous password list! {Passlist}")
    
    
