num = 220 - int(input("Age: ")) 
max = -1
min = 999
z3 = 0
z4 = 0
z5 = 0

while True:
    bpm = int(input("bpm: "))
    if bpm == 0:
        break

    if bpm >= (num * 0.9):
        z5 += 1
    elif bpm >= (num * 0.8):
        z4 += 1
    elif bpm >= (num * 0.7):
        z3 += 1

    if bpm > max:
        max = bpm
    if bpm < min:
        min = bpm

tot = z5 + z4 + z3
print("Results:\nZona3 (>",num * 0.7  ,"): ", round((z3/tot) * 100,2), "%\nZona4 (>",num * 0.8  ,"): ", round((z4/tot) * 100,2), "%\nZona5: (>",num * 0.9  ,"): ", round((z5/tot) * 100,2),"%")
print("Max:", max, "\nMin:", min)