class memory:
    def __init__(self,size):
        self.__SIZE=size
        self.used=0
        self.dic=[]
    def addword(self,word):
        if self.used^self.__SIZE:
            self.dic.append(word)
            self.used+=1
        else:
            self.dic.pop(0)
            self.dic.append(word)
    def check(self,word):
        if word in self.dic:
            return True
m,n=map(int,input().split())
mem=memory(m)
ans=0
for i in map(int,input().split()):
    if not mem.check(i):
        ans+=1
        mem.addword(i)
print(ans)