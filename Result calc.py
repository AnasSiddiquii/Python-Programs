a=int(input('Maths      :- '))
b=int(input('Science    :- '))
c=int(input('Computer   :- '))
d=int(input('History    :- '))
e=int(input('Economics  :- '))
print() # for line space

f=((a+b+c+d+e)/500)*100
print('Percentage :- ',f,'%')
print() # for line space

if 100>=f>=80:
    print('A Grade')
elif 79>=f>=60:
    print('B Grade')
elif 59>=f>=40:
    print('C Grade')
elif 39>=f>=0:
    print('Fail')
else:
    print('invalid')
print()