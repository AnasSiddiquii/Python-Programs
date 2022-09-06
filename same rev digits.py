while True:
    try:
        print()
        a=int(input('Enter no. :- '))
        b=0
        x=a

        while a!=0:
            c=a%10
            a=a//10
            b=b*10+c
        
        if b==x:
            print('Answer    :- Matched')
        
        else:
            print('Answer    :- Not Matched')

    except:
        print('Answer    :- Invalid')