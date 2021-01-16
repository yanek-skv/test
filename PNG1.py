# #курсив
# print("\033[31mhello world! \033[0m hhh")
# print("\033[4m Hellw wirld \033[0m eee")
# #2
# a=("""Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Integer euismod volutpat eleifend. Lorem ipsum dolor sit amet,
# consectetur adipiscing elit. In sed facilisis dui. Morbi gravida et nisi et
# luctus. Suspendisse lorem eros, viverra sit amet lacus rutrum, cursus
# consequat turpis""")
# print(len(a))
# print(a.count("o"))
# #колво слов
# print(a.count(" ")+1)
# #колво предложений
# print(len(a.split("."))-1)
# #посчитать lo
# print((a.lower()).count("lo"))
# #поменять lorem LOPE
# print(a.lower().replace("lorem", "LOPE"))
# #Треугольник
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# if a+b>c and a+c>b and b+c>a:
#     print('треугольник')
# else:
#     print('не треугольник')
# #Создайте список квадратов чисел от 0 до 10
# a=([i*i for i in range(0,10)])
# b=a.copy()
# n=tuple(i+5 for i in b)
# print(n)
# #Создайте словарь, где ключ - порядковый номер
# a=([i*i for i in range(0,10)])
# b=a.copy()
# n=tuple(i+5 for i in b)
# print(n)
# print(len(n))
# c={i+1: n[i] for i in range(len(n))}
# print(c)
# #Напишите функцию
# def aas(*args):
#     list1 = [i+"!" for i in args]
#     return list1
#
#
# str1='lorem'
# str2='ipsum'
# str3='dolor'
# str4='sit'
# l1=aas(str1,str2,str3,str4)
# print(l1)

# #Вылавливание ошибок обработка исключений, для данных вводом которых мы не владеем
# a=input('ввод ')
# try:
#     d=int(a)+3
#     print(d)
# #после except можно указать какая имено ошибка из списка изключений "expect valueerror"
# except:
#     print('не коррные данные')
# finally:
#     print('это выводится при любом исходе')

#задача ввода ФИО

#####first_name=input('ввидите имя: ')
#####last_name=input('Ввидите фвмилию: ')

def valid_name(first_name, last_name):
    if first_name.isalpha() and last_name.isalpha():
        if not first_name.istitle():
            first_name = first_name.title()
        if not last_name.istitle():
            last_name = last_name.title()
        return first_name, last_name
    else:
        print('ввидите корректные данные')
        return False

print(valid_name('1', 'скворцов'))




