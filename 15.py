#на количество А
count = 0
for a in range(1, 300):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if ((x < a) <= (x*x <100)) and ((y**2 <= 64) <= (y <= a)):
                k += 1
    if k == 90_000:
        count += 1
print(count)