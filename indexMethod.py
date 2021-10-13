myList = [1,2,3,2,3,3]

print(myList.count(1), myList.count(2), myList.count(3))

pos = 0
for i in range(0, myList.count(3)):
    i = myList.index(3, pos)
    print(i, end=" ")
    pos = i + 1
print()