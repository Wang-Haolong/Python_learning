def sandwich(*ingredients):
    '''describe the sandwich''' 
    print("It's made of",end=' ')
    for i in ingredients:
        print(i,end=',')
sandwich('meat','vegetable','bread')