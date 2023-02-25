#5100722
file = open('58173_16341460620930_doc.txt')
n=file.read().split()
l=len(n)
s=0
for i in range(l):
    m=int(n[i])
    if (m%2==0 and m%47==0 and m%3!=0 and m%19!=0):
        s=s+1
        print(m)
print(s)
