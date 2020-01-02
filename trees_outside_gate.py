len,m=map(int,input().split())
tree=[0 for i in range(len+1)]
for i in range(m):
    l,r=map(int,input().split())
    tree[l]+=1
    tree[r]-=1
sum=0
flag=0
for i in tree:
    if i==0 and flag==0:
        sum+=1
    else:
        flag+=i
print(sum)