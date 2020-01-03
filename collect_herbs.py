t,m=map(int,input().split())
val=[0 for i in range(t+1)]
for i in range(m):
    c,v=map(int,input().split())
    for j in range(c,t+1):
        val[j-c]=max(val[j-c],val[j]+v)
print(val[0])