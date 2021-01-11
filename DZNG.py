# #1
# b=[1,2,3,4,5,6,7]
# def middl_mas(a):
#     return sum(a)/len(a)
# print(middl_mas(b))
#
# #2
# def sot_s(s):
#     sot=(int(s % 1000 / 100))
#     return 'сотни',sot
# def des_d(d):
#     des=(int(d%100/10))
#     return 'десятки',des
# def ed_e(e):
#     ed=(int(e%10))
#     return 'единицы',ed
# def tis_t(t):
#     tis=(int(t/1000))
#     return 'тысячи',tis
#
# a=int(input('Введите любое число не больше 6 символов '))
# if a > 1000 or a == 1000:
#     print(tis_t(a))
#     print(sot_s(a))
#     print(des_d(a))
#     print(ed_e(a))
# elif a < 1000 and a > 99:
#     print(sot_s(a))
#     print(des_d(a))
#     print(ed_e(a))
# elif a < 100 and a > 9:
#     print(des_d(a))
#     print(ed_e(a))
# else:
#     print(ed_e(a))

# #3
# def sum_s(s):
#     d=0
#     for i in s:
#         d += int(i)
#     return 'сумма чиссла',s,'=',d
#
# a=input('ввидите натуральное число')
# print(sum_s(a))

# #4
# def month_to_season(m):
#     month={1:'январь',2:'февраль',3:'март',4:'апрель',5:'май',6:'июнь',7:'июль',8:'август',9:'сентябрь',10:'октябоь',11:'ноябрь',12:'декабрь'}
#     if m <= 0 or m > 12:
#         print('такого месяца нет')
#     else:
#         print('это месяц ',month[m])
#         if m == 1 or m == 2 or m == 12:
#             print('зима')
#         if m >= 3 and m <=5:
#             print('весна')
#         if m >= 6 and m <= 8:
#             print('лето')
#         if m >=9 and m <= 11:
#             print('осень')
#     return
# mount=int(input('введите номер месяца '))
# month_to_season(mount)
#
#6
# def count_st(x):
#     d2={}
#     l1=x
#     l2=list(set(l1))
#     for i in l2:
#         if l1.count(i) > 1:
#             d2[i]=l1.count(i)
#     if d2:
#         print(d2)
#
# print('Вводите по одному числу, для выхода наберите end')
# st=[]
# while True:
#    i=input()
#    st.append(i)
#    count_st(st)
#    if i == 'end':
#        break
#
#7
# a = float(input("first number "))
# c = float(input("two number "))
# b = str(input("operation "))
# if b == '/':
#     if c == 0:
#         print('Деление на 0!')
#     else:
#         print(a/c)
# if b == '+':
#     print(a+c)
# if b == '-':
#     print(a-c)
# if b == '*':
#     print(a*c)
# else:
#     print('Операция не поддерживается')
#
#8
def chet_v(h):
    if h%2 == 0:
        return (h)

h=[]
while True:
    f=int(input('ввидите число '))
    if chet_v(f):
        h.append(chet_v(f))
    if f == 123:
        break
    print(h)