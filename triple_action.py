def check(a,b,c):
    alln=[a,b,c]
    nums=[False,]
    for i in range(9):
        nums.append(True)
    for i in alln:
        while i:
            if nums[i%10]:
                nums[i%10]=False
            else:
                return False
            i=i//10
    return True
i=123
while i*3<999:
    if(check(i*1,i*2,i*3)):
        print(i*1,i*2,i*3)
    i+=1