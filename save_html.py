import requests
#goal=requests.get(input())
goal=requests.get(input(),headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
f=open(input(),'wb')
f.write(goal.text.encode(goal.encoding))
f.close()