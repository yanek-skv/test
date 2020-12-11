#задача1
z = int(input('введите z '))
x = int(input('введите x '))
if z % 2 == 0:
    print (z, 'чётное')
if x % 2 == 0:
    print (x, 'чётное')

#задача2
a = int(input('введите a '))
b = int(input('введите b '))
c = int(input('введите c '))
if a <= b <= c or c <= b <= a:
    print(b)
elif b <= a <= c or c <= a <= b:
    print(a)
else:
    print(c)

#задача3

a = int(input('введите a '))
b = int(input('введите b '))

if a % b == 0:
    print ('a делится на b =', a/b)
else:
    print ('a не делится на b, остаток=', a%b)

#задача 4
x = int(input('введите x '))
y = int(input('введите y '))

if x>0 and y>0:
    print('1 четверть')
elif x<0 and y>0:
    print('2 четверть')
elif x<0 and y<0:
    print('3 четверть')
else:
    print('4 четверть')

#задача5
print('a*x^2+b*x + c')
a = int(input('введите a '))
b = int(input('введите b '))
c = int(input('введите c '))
discr = b * b - 4 * a * c
print('D=', discr  )

if discr > 0:
    print('x1=', ((a * ((-b + discr**0.5) / (2 * a))) * (a * ((-b + discr**0.5) / (2 * a)))) + b * ((-b + discr**0.5) / (2 * a)) + c)
    print('x2=', ((a * ((-b - discr**0.5) / (2 * a))) * (a * ((-b - discr**0.5) / (2 * a)))) + b * ((-b - discr**0.5) / (2 * a)) + c)
elif discr == 0:
    print('x=', -b / (2 * a))
else:
    print('D < 0 решений нет')


#задача6
for i in range(101):
    print(i)
#задача7
for i in range(3,13):
    print(i*3*3)
#задача8
a=[1,2,3,4,5]
a[0]='a'
a[len(a)-1]='b'
print(a)
#звдача9
a=[1,2,3,4,5]
if a:
    for i in range(len(a)):
        if i%2 == 0:
            print(a[i]*2)
#задача10
p=[2,5,8,3,-1,-6]
print('макимум',max(p))
print('минимум',min(p))
s=0
for i in p:
    s+=i
print('сумма списка',s)

for i in p:
    if i < 0:
        print('отоицательные',i)

#задача11

week=['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
for i in range(len(week)):
    if i < 5:
        print(week[i])
    else:
        print('\033[1m{}' .format(week[i]))




