sum=int(input())
if sum<=150:
    print("%.1f" %(sum*0.4463))
elif sum<=400:
    print("%.1f" %((sum-150)*0.4663+150*0.4463))
else:
    print("%.1f" %((sum-400)*0.5663+150*0.4463+250*0.4663))
