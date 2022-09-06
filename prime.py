while True:
    
    try:
        print()
        a=int(input('Enter no. :- '))
        b=0

        if a>1:
            for i in range(2,a):
                if a%i==0:
                    b=b+1
                    break
        else:
            b=2
        
        if b==0:
            print('Answer    :- Prime')
        elif b==1:
            print('Answer    :- Not Prime')
        elif b==2:
            print('Answer    :- Invalid')          
        else:
            print('Answer    :- Invalid')

    except:
        print('Answer    :- Invalid')