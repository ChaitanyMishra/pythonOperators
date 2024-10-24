l1 = [[1,2],[2,3,4],[4,5,6,7,8,9,0],[1]]
temp2 = 0
for i in l1:
    if len(i) > temp2:
        temp = i
        temp2 = len(i)
print(f"maximum length list: {temp}")
print(f"Maximum length of sublist : {temp2}")