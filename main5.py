#гениратор списка
#итератор списка для создания конструкции данных в одну строчку i - то что кладётся в список for i для i - список или условие
#i for in range 10 - просто лист if i%2
#print([i for in week if i=='mondey'] [0])
#a=[i%10 for in i range(0,100,2)]  - на чтозаканчиваются числа от 0 до 100 с шагом 2
#!
#print([i%10 for i in range(0,100,2)])
#!
#print([i for in week if i=='mondey'] [0])  -  a=[i%10 for in i range(0,100,2)]
#a=[то что пойдёт в лист / то что с ним произайдёт  |  итарационный процесс for    |   условия (этого блока может не быть) if ]
#
# while нужен когда мы не знаем сколько оприаций в будущем while(условие):
#постусловие
#while true
#   if a%2 == 0
#   breack
#
#continue  - пропустить
#for i in range[1.10]
#    if i%5 == 0
#    continue
#    else
#    print(i)
#
#pass - ничего не делать- заглушка
#
# set dict tuple
#dict структура которая задаётся {key1:value, key2:value}  {'name':'nacty', 'age':'30'}
#!
#d.clear
#b={'age':30, 'name':'Pety','uni':12}
#print(b)
#print(b['name'])
#b['age']=40
#print(b)
#b1=b.copy() #копируем
#print(b.keys()) #список из всех ключей
#dict_kry=b.keys()
#print(dict_kry)
#print(b.items()) #ключь занчение - пара

#for key in b.keys():  #перебираем всё ключи
#    print(key, b[key]) #вызываем ключь, значение по ключу
#dict_key=[key for key in b.keys()] #создаём список из ключей
#print(dict_key[2])

#for i in b.items():  #выводит со скобками (ключ, значение)
#    print(i)

#for i,k in b.items():  #выводит без скобок - ключ значение
#    print(i,k)

#b.pop('age') # удалить по ключу
#b3={'we':'rr','dd':'ww'}
#print(b3)
#print(b)
#b.update(b3) #соединить словари
#print(b)
#!
#1ключи всегда разные,2 это не позиционный контенер, доступ по ключям - имясловоря['ключь'] если ключь в ковычках то так и пишем
#
buk={'pn':10,'wt':20, 'sr':30, 'ch':40, 'pt':50, 'sb':60, 'vs':70}  #сложить все значения из словоря
print(sum([buk[i] for i in buk.keys()]))  # перебирает все ключи for i in buk.keys()] - формирует список по ключям buk[i] - суммиреут список sum

#-2,17,10,7,7
ov={'yab':50, 'gru':20, 'kart':100, 'ogur':70, 'pomid':110}
ku={'yab':2, 'gru':17, 'kart':10, 'ogur':7, 'pomid':7}

for key in ku.keys():
    ov['key']=ov['key']-ku['key']
print(ov)

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
