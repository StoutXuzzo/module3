while True:
    capital = float(input("Input capital: "))
    interest = float(input("Input interest: ")) / 100
    year = int(input("Input years: "))
    time = year / 12
    paid = 0

    fransua = capital * ((interest * (1 + interest)**year) / (((1 + interest)**year) - 1))

    cont = 0
    while cont < year:
        cont += 1
        paid += fransua
        print("Year:", cont, "- quota:", round(fransua,2), "€ - Paid Out:", round(paid,2), "€")
    
    more = input("More opeations (Y/N): ")
    if more == "N":
        break