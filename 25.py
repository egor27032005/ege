for n in range(25,8701):
    sum=0
    t=1
    while n>t/2-1:
        if n%t==0:
            sum+=t
        t+=1
    if sum==n:
        print(n,t)
#Ответ: 2401 343