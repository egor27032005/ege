x = 87
s = ''
for i in range(2,10):
    s=''
    x=87
    while x != 0:
        s += str(x % i) 
        x //= i
    s = s[::-1]
    print(i,s)
