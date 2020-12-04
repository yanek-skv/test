
print("Task 1")
a=input("введите набор чисел больше 9-")
#print('числа с индекмом кратным 3-',a[::3])
print('числа с индекмсом кратным 3-',' '.join(a[::3]))
print('Task 2')
b='Тучки небесные, вечные странники! Степью лазурною, цепью жемчужную Мчитесь вы, будто как я же, изгнанник и Смилого севера всторону южную'
print(b)
print('меням Мчитесь на спешите')
print(b.replace('Мчитесь', 'спешите'))
print('Task 3')
print('количество запятых-',b.count(','))
print('количество пробелов-',b.count(' '))
print('Task 4')
print(b)
print('delete жемчужную')
print(b.replace('жемчужную', ''))
print('Task 5')
g='Дмитрий считает, что когда текст пишут в скобках (каквот тут, например), его читать не нужно.'
print(g)
print(g[:g.index('(')]+g[g.index(')')+1:])
print('Task 6')
e='несколько слов через пробел'
print(e)
h=e.split()
print('!!!'.join(h))
print('***'.join(h))
print('Task 7')
y='П@Р!!!и?в)))))еТ: к00АК^ дЕлА'
print(y)
ys=y.split(' ')
print(((''.join(filter(str.isalpha, ys[0]))).lower())+' '+((''.join(filter(str.isalpha, ys[1]))).lower())+' '+((''.join(filter(str.isalpha, ys[2]))).lower()) )

#  В одну строку
y='П@Р!!!и?в)))))еТ: к00АК^ дЕлА'
print(((''.join(filter(str.isalpha, y.split(' ')[0]))).lower())+' '+((''.join(filter(str.isalpha, y.split(' ')[1]))).lower())+' '+((''.join(filter(str.isalpha, y.split(' ')[2]))).lower()))





