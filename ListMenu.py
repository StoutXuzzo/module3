list = []

while True:
    print("\nMENU")
    print("---------------------------------------------------------")
    print("1.- Add a number to the list.")
    print("2.- Add a number in a position in the list.")
    print("3.- Show the length of the list.")
    print("4.- Delete the last number in the list.")
    print("5.- Delete a number in the list.")
    print("6.- Count numbers.")
    print("7.- Positions of a numbers.")
    print("8.- Show the list.")
    print("9.- Exit.")
    print("---------------------------------------------------------")
    option = input("\nSelect an option: ")

    if option == "1":

        while True:
            num = input("Insert the number you want to add: ")
            if num.isdigit():
                num = int(num)
                list.append(num)
                break
            else:
                print("You only can insert numbers in the list.")

    elif option == "2":

        while True:
            num = input("Insert the number you want to add: ")
            pos = input("Insert the position where you want that number: ")
            if num.isdigit() and pos.isdigit():
                num = int(num)
                pos = int(pos)
                list.insert(pos-1, num)
                break
            else:
                print("You have to insert numbers.")

    elif option == "3":

        print("The list is", len(list), "numbers long.")

    elif option == "4":

        del list[-1]

    elif option == "5":
    
        num = input("Insert the position you want to delete:")
        if num.isdigit():
            num = int(num)
            if num > len(list):
                print("This position does not exist.")
            else:
                del list[num-1]
    
    elif option == "6":
    
        while True:
            num = input("Insert a number: ")
            if num.isdigit():
                num = int(num)
                cont = 0
                for listNum in list:
                    if listNum == num:
                        cont += 1
                print("Your number is", cont, "time in the list.")
                break
            else:
                print("You have to insert a number.")

    elif option == "7":

        postList = []
        while True:
            num = input("Insert the number:")
            if num.isdigit():
                num = int(num)
                for i in range(len(list)):
                    if num == list[i]:
                        postList.append(i+1)
                if len(postList) > 0:
                    print("The number is in the next positions:", postList)
                else:
                    print("The number isn't in the list.")
                break
            else:
                print("You have to insert a number.")

    elif option == "8":

        print("Values of the list:", list)

    elif option == "9":

        print("That's All Folks!")
        break

    else:
        print("Please, select a valid option.")