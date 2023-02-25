def F(n):
    if n<2:
        return 1
    elif n>1 and n%2==1:
        return F(n-2)+n
    elif n>1 and n%2==0:
        return F(n-1)*n

print(F(84))
##Алгоритм вычисления функции F(n) задан следующими соотношениями:

##F(n) = 1 при n ≤ 1;
##F(n) = n · F(n – 1) при чётных n > 1;
##F(n) = n + F(n – 2) при нечётных n > 1;

