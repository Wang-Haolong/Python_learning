import requests
headers=headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
goal=requests.get(input(),headers=headers)
#伪iphone6:
#goal=requests.get(input(),headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
f=open(input(),'wb')
f.write(goal.text.encode(goal.encoding))
f.close()