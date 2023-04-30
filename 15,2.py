for a in range(900, 0, -1):
    k = 0
    for x in range(1, 1000):
        if (x % a == 0) <= ((x % 33 == 0) or (x % 55 == 0)):
            k += 1
    if k == 999:
        print(a)
        break
