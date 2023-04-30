##9**
x = 9**200+3**100-7
s = ''
while x != 0:
    s += str(x % 3) 
    x //= 3
s = s[::-1]
print(s.count("2"))
