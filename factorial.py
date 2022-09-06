while True:
    try:
        print()
        a=int(input('Enter no. :- '))
        b=1
        
        while a!=0:
            c=a%10
            a=a//10
            b=b*c
        
        print('Answer    :-',b)

    except:
        print('Answer    :- Invalid')