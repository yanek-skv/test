#объединить 2 словоря
# d1={1:'1', 2:'2'}
# d2={3:'3', 4:'4'}
# d2.update(d1)
# print(d2)

# d3={i:i**3 for i in range(0,11)}
# print (d3)

# scool={'1a':20, '2b':30, '3e':40}
# sum=0
# mul=1
# for key in scool.keys():
#     sum=scool[key]+sum
# print(sum)

# !
# sc={'1a':20, '2b':30, '3e':40}
# print(sum([val for val in sc.values()]))
#!

#a=[1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,7,7,7,7,7]
#d1={1:'1', 2:'2', 3:'3', 4:'7'}
#b2={'1':5,'2':6,'3':4,'4':5}

# p='pytonist'
# d={char:p.count(char) for char in p}
# print(d)


#ножество картедж set yupl
# типы коллекций изменяемые set dict{} list[] не изменяемые str tuple()
#Множество коллекция не одинаковых элеменов

# l1 = [i for i in range(1,1001)]
# t1 = (i for i in range(1,1001))
# print(l1.__sizeof__())
# print(t1.__sizeof__())

# a=tuple()
# b=('c',)
# print(type(b))
#
# #распаковка кортеджей
# a=1
# b=2
# print(a, b)
# a, b = b, a
# print(a, b)

# list1=[1,11,2,3]
# a=tuple(list1)
# print(a)

#множество {} выстраевает по порядку

# list2=[3,1,2,2,23]
# print(set(list2))
# print(len(set(list2)))

# a={i for i in range(1,10)}
# print(a)

# set1={1,2,3,4,5,6,7,8}
# set2={4,5,6,7,8,9,3,2}
# #есть ли элимент в множестве
# print(3 in set1)
# #равенство множеств
# print(set1 == set2)
# #все ли элементы 1го содаржатся во втором
# print (set1<=set2)
# #щбъединение
# print(set1 | set2)
# #пересичение
# print(set1 & set2)
# #добавить элимент
# set1.add(11)
# print(set1)
# #удалить
# set1.remove(11)
# print(set1)

#функция def name_function(аргументы):
#    return результат

# def speaker_hello_world():
#     print('Hello World')
#     return
# speaker_hello_world()

# def sume():
#     a=3
#     b=4
#     s = a+b
#     return s
# s=sume()
# print(s, sume())

# def lising_st():
#     a='hello i know more python'
#     b=list(a)
#     print(type(b))
#     return len(b)
# a = lising_st()
# print(a)


def suma_dele():
    a=10
    b=3
    c=a+b
    g=a%b
    e=a*b
    return c,g,e
print(suma_dele())