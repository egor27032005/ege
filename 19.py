def f(x, h): 
    if h == 3 and x >= 84:
        return 1

def f(x, h):
    if h == 3 and x >= 84:
        return 1
    elif h == 3 and x < 84:
        return 0
    elif x >= 84 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 4, h + 1) or f(x * 5, h + 1)or f(x +1, h + 1)   # стратегия победителя
        else:
            return f(x * 5, h + 1)#and f(x + 1, h + 1)  # стратегия проигравшего(любой ход)
 
for x in range(1, 84):
    if f(x, 1) == 1:
        print(x)
        break