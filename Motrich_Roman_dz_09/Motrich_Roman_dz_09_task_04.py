'''
4. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw()
(отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три производных класса Pen (ручка), Pencil (карандаш),
 Handle (маркер);
в каждом классе переопределить метод draw(). Для каждого
класса метод должен выводить уникальное сообщение;
создать экземпляры каждого класса и положить их в список.
Проитерироваться по этому списку и вызвать метод draw() для каждого элемента.
'''

class Stationery:
    title=None

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        print('Запуск отрисовки ручки')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print('Запуск отрисовки карандаша')


class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        print('Запуск отрисовки ручки')


stationeryes=[Stationery(),Pen(),Pencil(),Handle()]
for i in stationeryes:
    i.draw()
