import hashlib
word=input()
code=hashlib.sha3_512()
code.update((word+'abcorsomethingelse').encode('utf-8'))
print(code.hexdigest())