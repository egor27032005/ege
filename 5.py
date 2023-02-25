for n in range(1, 50):
    r=str(bin(n)[2:])
    if n%2==0:
        r=r+'11'
    else:
        r=r+'00'
    if int(r,2)>70:
        print(int(r,2))
