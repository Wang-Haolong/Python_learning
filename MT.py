m,n=map(int,input().split())
mem=[]
ans=used=0
for i in filter(lambda x:x not in mem,map(int,input().split())):
        if not len(mem)^m:mem.pop(0)
        mem.append(i)
        ans+=1
print(ans)