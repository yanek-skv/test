
#list1=[]
#list1.append('привет')
#list1.append(1)
#list1.append(['hello', 'world'])
#print(list1)
#list1.extend('4')
#print(list1)
#list1.insert(0, 'glow')
#list1.insert(20, 'glow')
#print(list1)
#удоляет первое одно вхождение (может дать ошибку)
#list1.remove('glow')
#print(list1)
#удаление по индексу (может дать ошибку)
#list1.pop(1)
#print(len(list1))

#print(reversed(list1))
#вывод <list_reverseiterator object at 0x0000027374A4FDD8>
#list1.clear()
#print(list1)

#a,b=1,2
# a1,b1 = [3,2,5, 'hello'] !!
#хронятся в одном месте памяти при изменение a меняется и b
#a1=b1=[3,5,5,'hello']
#разделяем места в памяти
#b1=a1.copy()

# Выаод
#разделитель переход строки
#end=' ' объединяет
#print(a1,b1)
#print(a1,b1, sep='\n')

# Синтаксические конструкции
#a=int(input('введи число-'))
#if a <= 10:
#    print('hello')
#elif a > 10 and a < 20:
#    print('hello user')
#else:
#    print('sello ***')

#треугольник
#a=int(input('a='))
#b=int(input('b='))
#c=int(input('c='))

#if a+b>c and a+c>b and b+c>a:
#    print('треугольник')
#else:
#    print('не треугольник')
# циклы
# for i in range(n):
a=[1,20,30,40]
for i in a:
    print(i+5)
# if a:   (a если списаок,число,строка а не пустной)
f=list(input())
print(f)
for i in f:
    print(int(i)+5)
