#l1=[1,1,1,1,1,2,2,2,2,7,7,7,10,10,10,10,8,8,8,8,8]
#d1={}
#s1=set(l1)
#l2=list(s1)
##d1{page:number_of-cottegoy}
#for i in range(1, len(l2)+1):
#    d1[i]=l2[i-1]
#print(d1)

#d1={i+1: l2[i] for i in range(len(l2))}
#print(d1)


#d2={}
#l1=[1,1,1,1,1,2,2,2,2,7,7,7,10,10,10,10,8,8,8,8,8]
#l2=list(set(l1))
#for i in l2:
#    d2[i]=l1.count(i)
#print(d2)

#параметры это то что передать в функцию при создание, аргументы это то что мы можем передать при вызове (позиционные)


#def mul(a,b):
#    return a*b
#print(mul(2, 3))
#print(mul(7, 5))

#def ost(f):
#    return f%3
#print(ost(10))


#def about_string(string):
#    l = len(string)
#    s1=string.upper()
#    s2=string.lower()
#    return l,s1,s2
#print(about_string('KKkkklL'))
#print(about_string('SSssrtyghh3'))


#def dik(a, b):
#     a.update(b)
#     return a
#print(dik({1:2,3:4}, {3:4, 6:7}))


##именованные аргументы заданые по дефолту
#def am(name='sveta', age=22):
#    print(name, age)
#    pass

#am()
#am(name='lene')
#am(age=33)


#def bn(name='no name', age=10):
#    name1 = name.upper()
#    age = age + 5
#    return name1, age
#print(bn(name='sveta', age=12))

##неизвестное кол-во аргументов > def name_fan(*args):   *задаёт кортедж

#def sumer(*args):
#    sum1 = sum(args)
#    return sum1
#print(sumer(2,6,8,9,7,))
#print(sumer(1))
#print(sumer())


#def name_fan(**kwargs):
#    print(kwargs)
#    pass
#name_fan(name='sveta', name2='lena')
#name_fan()

#file > seting > inprotritetor > projekt > python intorpritator > + в углу ( открывает все сторонние библиотеки)

# https://py.checkio.org/

