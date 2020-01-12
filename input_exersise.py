print('Let me see if I can find you a '+input('What car do you want? ')+'.')
if int(input('How many persons will have meal? '))>8:
    print('We have no free table now.')
else:
    print('We have a free table right now.')
num=int(input('Type in a number: '))
if num%10:
    print(str(num)+" is'nt a multiple of 10")
else:
    print(str(num)+" is a multiple of 10")