import pickle
class test:
    def __init__(self):
        self._name='TEST'
        self.word='Hello World!'
add=input()
f=open(add,'wb')
d=test()
pickle.dump(d,f)
f.close()
f=open(add,'rb')
print(pickle.load(f).word)
f.close()