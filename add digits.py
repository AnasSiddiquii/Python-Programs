while True:

    try:
        print()
        a=int(input('Enter no. :-  '))
        b=0

        while a!=0:
            # a = 128
            c=a%10    # 8
            a=a//10   # 12.8 > 12
            b=b+c     # 0 + 8

        print('Answer    :- ',b)
  
    except:
        print('Answer    :-  Invalid')