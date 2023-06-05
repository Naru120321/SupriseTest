a=list(map(int,input().split()))
b=[0]*len(a)
p=0
for i in range(len(a)):
    if a[i]!=0:
        b[p]=a[i]
        p=p+1
print(b)