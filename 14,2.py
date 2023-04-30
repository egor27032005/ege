y = "0123456789AB"
for x in y:
    a = "19"+x+"61"
    b = "3393"+x
    c="60"+x+"05"
    a = int(a, 12)
    b = int(b, 17)
    c = int(c, 15)
    if a+b==c:
        print(x,a+b)