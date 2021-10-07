myList = [10,2,3,4,4,4,3,3,3,5,6,7]
newList = []

for i in myList:
    if i not in newList:
        newList.append(i)

print(myList)
print(newList)