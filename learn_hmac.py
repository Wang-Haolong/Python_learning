import hmac
word=input()
key=b'abcorelse'
h=hmac.new(word.encode('utf-8'),key,digestmod='SHA512')
print(h.hexdigest())