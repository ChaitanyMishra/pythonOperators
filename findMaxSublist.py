l1 = [[1,2],[1,2,3,4,6,7,3],[1,2,3,4]]
temp2 = 0
for i in l1:
    if len(i) > temp2:
        temp = i
        temp2 = len(i)
print(f"maximum length list: {temp}")
print(f"Maximum length of sublist : {temp2}")