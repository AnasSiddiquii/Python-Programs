while True:

    try:
        print()
        a=int(input('Enter no. :- '))
        if a%2==0:
            print('Answer    :- Even')
            print()
        else:
            print('Answer    :- Odd')

    except:
        print('Answer    :- Invalid')