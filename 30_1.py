## вариант1  создания аиртуальной среды
## нев продект - ню либо ексайтинг ( создание виртуальной среды)если нев выбираем папку кудп сделать копию
## если екзистинг то выбераем откуда берём существующую папку
## варивнт 2
## находимся в папке file-settings-progekt intopritator-showall- +
## проверяем/запускаем что всё ок run - edit configuration - поле пайтен инторпиритатор выбераем копию жмём ОК
## либо просто проверить импорт пакета.


##функия может быть переменной
# def y(x):
#     return x*x
#
# def join1(l, func):
#     for i in l:
#         print(func(i))
#
# l = [1,2,3,4,5]
## в переменную y передаём название вункции y которая помещается в print(func(i)) функия может быть переменной
# join1(l, y)

## lambda однострочная функция (слева аргументы справа возращение x,y:x+y)
# a=lambda x:x*x
# print(a(5))

## функция map принимает этирабельный объект map(функция,это бъект list,str,dict) оплучем чтото типа range
# def y(x):
#     return x*x
# l=[1,2,3,4]
# print(map(y,l))
# for i in map(y,l):
#     print(i)

## практика  в эту функию засовывает ренж

# a=lambda x:x+5
# print(a(5))
#
# for i in map(a, [1,2,3,4,5]):
#     print(i)
#
# l=[5,7,9]
# for i in map(a, l):
#     print(i)

## алгоритм сортировки

## сортировка пузырьком
# l=[1,4,6,8,9,110,24,10]
# for i in range(len(l)-1):
#     for j in range(len(l)-1):
#         if l[j] > l[j+1]:
#             a = l[j]
#             l[j]=l[j+1]
#             l[j+1]=a
# print(l)

## прошлое дз проверка валидности почтового адреса
def valid_email(email):
    if not '@' in email:
        return False
    if email.count('.') or email.count('.') < 1:
        return False
    k=['!','#','%']
    for i in k:
        if i in email:
            return False
    return email,True
valid_email(ad@e1.ru)





