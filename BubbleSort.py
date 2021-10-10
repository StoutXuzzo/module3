myList = [8,2,3,4,1,5,6]

i = 0
while i < len(myList):
    j = 0
    while j < len(myList):
        if myList[j] > myList[i]:
            myList[i], myList[j] = myList[j], myList[i]
        j += 1
    i += 1
    
    
print(myList, i)

myList = [8,2,3,4,1,5,6]
i = 0
semaf = True
while semaf:
    i+=1
    semaf = False
    for index in range(len(myList)-1):
        if myList[index] > myList[index+1]:
            myList[index], myList[index+1] = myList[index+1], myList[index]
            semaf = True
print(myList,i)
