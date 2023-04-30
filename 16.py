def F(n):
    if n<2:
        return n
    elif n%2==0 and n>1:
        return F(n-1)+F(n-3)
    elif n%2==1 and n>1:
        return F(n-2)*n

       
print(F(13))
##Алгоритм вычисления функции F(n) задан следующими соотношениями:

##F(n) = 1 при n ≤ 1;
##F(n) = n · F(n – 1) при чётных n > 1;
##F(n) = n + F(n – 2) при нечётных n > 1;

