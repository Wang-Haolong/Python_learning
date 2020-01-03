def times(name):
    ans=1
    for i in name:
        ans*=ord(i)-64
    return ans%47
if times(input())^times(input()):print('STAY')
else:print('GO')