size = int(input("Enter size of loop: "))
print("Enter '1' for assending sort '2' for desending")
choice = int (input("Enter your choice: "))
if choice == 1:
    num_1 = int(input("Index 1: "))
    for i in range(2 , size+1):
        num = int(input(f"Index {i}: "))
        num = num_1
        temp = num
        if num > temp:
            temp_2 = num
            temp = temp_2
        else:
            continue
    for i in range(1 , size+1):
        print(num , end = " ")
elif choice == 2:
    num_1 = int(input("Index 1: "))
    for i in range(2 , size+1):
        num = int(input(f"Index {i}: "))
        num = num_1
        temp = num
        if num < temp:
            temp_2 = num
            temp = temp_2
        else:
            continue
for i in range(1 , size+1):
    print(num , end = " ")
      
    