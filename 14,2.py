y = "0123456789ABC"
for x in y:
    a = "42A"+x+"1"
    b = "B"+x+"81"
    a = int(a, 13)
    b = int(b, 13)
    if (a-b) % 9 == 0:
        print(x, (a-b) // 9)