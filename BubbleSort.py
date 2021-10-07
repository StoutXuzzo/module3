myList = [8,2,3,4,5,6]
semaf = False

i = 0
while i < len(myList):
    j = 0
    while j < len(myList):
        if myList[j] > myList[i]:
            myList[i], myList[j] = myList[j], myList[i]
            semaf = True
        j += 1
        #if semaf == False:
        #    break
        semaf = False
    i += 1
    print(i)
print(myList)

myList = [8,2,3,4,5,6]

semaf = True
while semaf:
    semaf = False
    for index in range(len(myList)-1):
        if myList[index] > myList[index+1]:
            myList[index], myList[index+1] = myList[index+1], myList[index]
            semaf = True
print(myList)
