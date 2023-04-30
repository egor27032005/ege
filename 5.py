for n in range(0, 50):
    r=str(bin(n)[2:])
    if n%2==0:
        r=r+"001"
    else:
        r=r+"100"
    if int(r,2)<350:
        print(int(r,2),n)
    