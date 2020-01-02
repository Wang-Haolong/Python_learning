maxn=[0,8]
for i in range(7):
    a,b=map(int,input().split())
    if a+b>maxn[1]:
        maxn[0]=i+1
        maxn[1]=a+b
print(maxn[0])