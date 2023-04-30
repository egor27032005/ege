sum=0
for Y in range(5):
    for E in range(80):
        def f(x, y,h):
            if x > y or h>5:
                return 0
            if x == y:
                return 1
            else:
                return f(x+1, y,h+1)+f(x*2,y,h+1)+f(x+x%4,y,h+1)
        if f(E, 80,Y)!=0:
            sum+=f(E, 80,Y)
            print(f(E, 80,Y))
print(sum)