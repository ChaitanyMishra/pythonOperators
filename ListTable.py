table = []
temp = 0
size = int(input("how much element you want to store? "))
while temp != size:
    data = input("Enter a value: ")
    table.append(data)
    temp +=1
for i in table:
    if i.isdigit():
        num = int(i)
        if num > 0:
            print(f"\nMultiplication table for {num}:")
            for j in range(1, 11):
                print(f"{num} x {j} = {num * j}")
    else:
        print(f"\n{i} is not a positive integer.\n")
