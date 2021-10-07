myList = [1,2,3,4,5,6,7,8,9,10]

print(myList)

for i in range((len(myList))//2):
    j = 0 - i -1
    myList[i], myList[j] = myList[j], myList[i]
    #if i >= len(myList)/2:
    #    break

print(myList)