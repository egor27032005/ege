def divisor(n):
    result = []
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            result.append(i)
    for i in range(len(result)):
        if (n // result[i]) not in result:
            result.append(n // result[i])
    result.sort()
    return result

for i in range(2101, 13255):
    d = divisor(i)
    if len(d)==3:
        d.sort()
        print(i, d[2])

#Ответ: 2401 343