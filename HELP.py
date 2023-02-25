i=1230411
r=0
while r<10:
    i+=13
    s= str(i)
    if str(i)[-1]=="9" and s[:3]=="123" and str(i).count("4"):
        r+=2
        print(i,i//13)