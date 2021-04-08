'''
5. Реализуйте базовый класс Car.
при создании класса должны быть переданы
атрибуты: color (str), name (str).
реализовать в классе методы: go(speed),
stop(), turn(direction), которые должны
 изменять состояние машины - для хранения
 этих свойств вам понадобятся дополнительные
 атрибуты - придумайте какие.
добавьте метод is_police() - который возвращает
True/False, в зависимости от того является ли
 этот автомобиль полицейским (см.дальше)
Сделайте несколько производных классов: TownCar,
SportCar, WorkCar, PoliceCar;
Добавьте в базовый класс метод get_status(), который
должен возвращать в виде строки название, цвет,
текущую скорость автомобиля и направление
движения (в случае если автомобиль едет), для
полицейских автомобилей перед названием автомобиля
должно идти слово POLICE;
Для классов TownCar и WorkCar в методе get_status()
рядом со значением скорости должна выводиться фраза
"ПРЕВЫШЕНИЕ!", если скорость превышает 60 (TownCar) и 40 (WorkCar).
Создайте по одному экземпляру каждого производного класса.
В цикле из 10 итераций, для каждого автомобиля сделайте одно из
случайных действий: go, stop, turn со случайными параметрами.
После каждого действия показывайте статус автомобиля.
'''
import random


class Car:
    def __init__(self, color, name):
        self.color=color
        self.polis_car=False
        self.speed=0
        self.name=name
        self.turned='Химки'
        self.speed_lim=None


    def go(self,speed):
        self.speed=speed

    def stop(self):
        self.speed=0

    def turn(self,turned):
        self.turned=turned

    def is_police(self):
        return self.polis_car

    def get_status(self):
        interpol='POLICE' if self.is_police() else ''

        if self.speed> 0:
            if self.speed_lim and self.speed>self.speed_lim:
                warning='Превышение'
            else:
                warning =''# 'Скоростной режим соблюдён'
            return f'{self.color} {self.name} движется со скоростью {self.speed} на {self.turned}, {warning} {interpol}'
        else:
            return f'{self.color} {self.name} стоит {interpol}'

class   TownCar(Car):
    def __init__(self, color, name):
        self.color=color
        self.polis_car=False
        self.speed=100
        self.name=name
        self.turned='Химки'
        self.speed_lim=60

class   SportCar(Car):
    def __init__(self, color, name):
        self.color=color
        self.polis_car=False
        self.speed=100
        self.name=name
        self.turned='Химки'
        self.speed_lim=None

class   WorkCar(Car):
    def __init__(self, color, name):
        self.color=color
        self.polis_car=False
        self.speed=100
        self.name=name
        self.turned='Химки'
        self.speed_lim=40


class   PoliceCar(Car):
    def __init__(self, color, name):
        self.color=color
        self.polis_car=True
        self.speed=100
        self.name=name
        self.turned='Химки'
        self.speed_lim = None




cars=[TownCar('Белый','Мазда'),
TownCar('Синий','Мицубик'),
TownCar('Красный','Калина'),
PoliceCar('Серый','УАЗ'),
WorkCar('Оранжевый','Камаз')
]

for i in range(10):
    for car in cars:
        action=random.randint(1,3)
        if action==1:
            car.go(random.randint(0,100))
        elif action==2:
            car.turn(random.choice(['Запад','Север','Восток','Юг']))
        elif action==3:
            car.stop()
        print(car.get_status())