def change(amount):
    lis=[]
    x5,x7=0,0
    while (amount<=1000):
        if(amount%7==0):
            x7=amount//7
            break
        else:
            amount-=5
            x5+=1
    for i in range(x5):
        lis.append(5)
    for i in range(x7):
        lis.append(7)
    return(lis)


print(change(500))