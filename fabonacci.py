while True:
    try:
        print()
        a=int(input('Enter no. :- '))
        b,c,x=0,1,0
        count=0

        for i in range(a):
            d=b+c
            b=c
            c=d
            x=x+1
        
        print(a)

    except:
        print('Answer    :- Invalid')