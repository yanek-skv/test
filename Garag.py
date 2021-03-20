import sys
from lib1 import *


car1=Gruz_Transort('kamaz', 20)
car2=Gruz_Transort('zil', 25)
car3=Gruz_Transort('maz',30)
car4=Gruz_Transort('volga', 10)
car5=Gruz_Transort('lada', 5)

my_garage=Garaz('my', 15)
my_garage.add_to_garag(car1.marks, car1)
my_garage.add_to_garag(car2.marks, car2)
my_garage.add_to_garag(car3.marks, car3)
my_garage.add_to_garag(car4.marks, car4)
my_garage.add_to_garag(car5.marks, car5)

print(my_garage.garaze)
my_garage.chek()


while True:
    try:
        need_tonn = int(input('ввидите нужно кол во тон'))



        sys.exit()
    except ValueError:
        print('введено не вероное кол-во тонн, попробуй заново')




