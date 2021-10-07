myList = [1,2,3,4,5]
print("All the list: ")
print(myList)

print("Only one position of the list: ")
print(myList[0])
print(myList[1])

print("Inverse numbers invers the order, -1 takes the last number and -2 the number befor the last: ")
print(myList[-1])
print(myList[-2])

print("Sliced list: ")
print(myList[1:3])
print(myList[2:])
print(myList[:3])

print("From 0 to the last number of the list minus 1: ")
print(myList[:-1])

print("The length of a list: ")
print(len(myList))

print("Delete a value: ")
print(myList)
del myList[2]
print(myList)
print("The new length of the list: ")
print(len(myList))
print("The position disapear, not only delete the value of the position, it delete the postion.")

print("The list is an object, and it have methods: (.append() and .insert())")
print("With .append() we put the number we give him in a new last positon: ")
print("After --> length:", len(myList), "Last Number:", myList[-1])
myList.append(69)
print("Befor --> length:", len(myList), "Last Number:", myList[-1])

print("With .insert() we have to give the metod 2 values, the position where we want to do the insert and the value: ")
print("After --> length:", len(myList), "Second Number:", myList[1])
myList.insert(1, 69)
print("Befor --> length:", len(myList), "Second Number:", myList[1])

print("The list can have diferent types in it: ")
myList.insert(0, "Hello!!")
print(myList[0])
