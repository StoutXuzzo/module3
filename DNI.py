code = "TRWAGMYFPDXBNIZSQVHLCKE"
semaf = False

while semaf == False:
    dni = input("Insert your DNI: ")
    dniNum = dni[:-1]

    if dni[:-1].isdigit() and len(dni) == 9:

        dniNum = int(dniNum)

        num = dniNum % 23
        if dni[-1] == code[num]:
            print("The dni is correct.")
        else:
            print("The dni is incorrect.")
        semaf = True
    else:
        print("You have to insert a correctly formated dni.")
