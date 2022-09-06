while True:

    try:
        print()
        a=int(input('Enter no. :- '))
        b=0

        while a!=0:
            # a = 123
            c=a%10  
            a=a//10
            b=b*10+c # 0*10+3=3 > 3*10+2=32 > 32*10+1=321
        
        print('Answer    :-',b)

    except:
        print('Answer    :- Invalid')