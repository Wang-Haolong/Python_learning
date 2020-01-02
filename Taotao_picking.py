apple=map(int,input().split())
high=int(input())+30
sum=0
for i in apple:
    if i<=high:sum+=1
print(sum)