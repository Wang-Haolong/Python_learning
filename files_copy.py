address=input()
with open(address,'rb') as f:
    l=len(address)-1
    while True:
        if address[l]=='.':break
        elif l==0:
            print("file name error")
            break
        l-=1
    with open(address[:l]+' - copy'+address[l:len(address)],'wb') as goalfile:
        goalfile.write(f.read())
print("done")