def f(x, h): 
    if h == 3 and x >= 23:
        return 1

def f(x, h):
    if h == 3 and x >= 23:
        return 1
    elif h == 3 and x < 23:
        return 0
    elif x >= 23 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 2, h + 1) or f(x * 2, h + 1)or f(x +1, h + 1)   # стратегия победителя
        else:
            return f(x + 2, h + 1) and f(x * 2, h + 1)and f(x + 1, h + 1)  # стратегия проигравшего(любой ход)
 
for x in range(1, 23):
    if f(x, 1) == 1:
        print(x)
        break