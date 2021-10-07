# Prompt the user to enter a word
# and assign it to the user_word variable.
msj = input("Write something: ")
msj = msj.upper()

for letter in msj:
    
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    print(letter)