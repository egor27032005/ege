def f(x, y, h):
    if h == 4 and x + y >= 83:
        return 1
    elif h == 4 and x + y < 83:
        return 0
    elif x + y >= 83 and h < 4:
        return 0
    else:
        if h % 2 != 0:
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1) or f(x * 2, y, h + 1)   # стратегия победителя
        else:
            return f(x + 1, y, h + 1) and f(x, y + 1, h + 1) and f(x, y * 2, h + 1) and f(x * 2, y, h + 1)  # стратегия проигравшего(любой ход)
 
for x in range(1, 74):
    if f(x, 9, 1) == 1:
        print("Задача 20:", x)