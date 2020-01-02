i=0;
week=[8]
maxn=[0,8]
while i<7:
    i+=1
    a,b=input().split()
    a=int(a)
    b=int(b)
    week.append(a+b)
    if week[i]>maxn[1]:
        maxn[1]=week[i]
        maxn[0]=i
print(maxn[0])
