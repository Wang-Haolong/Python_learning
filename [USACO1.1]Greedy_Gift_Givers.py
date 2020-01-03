class person:
    def __init__(self,name):
        self._name=name
        self._money=0
n=int(input())
d=[]
for i in range(n):
    d.append(person(input()))
for i in range(n):
    name=input()
    mon,fri=map(int,input().split())
    for j in d:
        if j._name==name:
            if fri:j._money+=mon%fri-mon
            break
    if fri:
        mon//=fri
        for j in range(fri):
            fname=input()
            for k in d:
                if k._name==fname:
                    k._money+=mon
                    break
for i in d:
    print(i._name.strip(),i._money)