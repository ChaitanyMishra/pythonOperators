money = float(input("how much money you want to deposit? "))
print("Enter number of Notes you depositing! ")
#-----------------------------------------------------------------------------
while True:
    note500 = int(input("How many $500 notes are you depositing? "))
    note200 = int(input("How many $200 notes are you depositing? "))
    note100 = int(input("How many $100 notes are you depositing? "))
    note50  = int(input("How many $50 notes are you depositing? "))
    note20  = int(input("How many $20 notes are you depositing? "))
    note10  = int(input("How many $10 notes are you depositing? "))
    #--------------------------------------------------------------------------------
    totalAmount = (note500 * 500) + (note200 * 200) + (note100 * 100) + (note50 * 50) + (note20 * 20) + (note10 * 10)
    if totalAmount == money:
        print(f"\nYou are depositing a total of ${totalAmount}...")
        break
    elif totalAmount < money:
        print("Your provided money is Less then your depositing money: ")
        temp = money - totalAmount
        print(f"add {temp} rupees extra! ")
    else:
        temp2 = totalAmount - money
        print("your provided money is higher then depositig money! ")
        print(f"remove {temp2} rupees! ")
    print("do you want to edit your notes order? ")
    ask = int(input("Enter '1' to continue... "))
    if ask != 1:
        print("Invalid input!\n exiting... ")
        break
