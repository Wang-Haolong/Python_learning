goal=float(input())
step=2
i=0
while goal>0:
    goal-=step
    step*=0.98
    i+=1
print(i)