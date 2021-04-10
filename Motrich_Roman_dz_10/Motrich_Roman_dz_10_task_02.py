'''
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Создать абстрактный класс Clothes (одежда). Сделать в этом классе свойство cloth_size
(используя декоратор @property) - размер ткани, необходимый для производства одежды.
Это свойство должно вычислять размерт ткани, вызывая абстрактный метод self.get_size().
Сделать два производных класса одежды: Suit (костюм) и Coat (Пальто).
В конструктор Suit должен принимать параметр height (рост), а Coat - size (размер).
Для определения расхода ткани по каждому типу одежды внутри метода get_size() использовать формулы:

для пальто: (size/6.5 + 0.5)
для костюма: (2*height + 0.3)
Создать список из 10 единиц одежды случайно выбирая один из двух возможных типов со случайным параметром.
Распечатать список одежды: размер требуемой ткани, тип и параметр.
Рассчитать и вывести на экран общий объем ткани, необходимый для пошива всей одежды из этого списка, используя свойство cloth_size. Например:

30.3 - Suit (height: 15)
20 - Coat (size: 3)
13.5 - Coat (size: 2)
4.3 - Suit (seze: 2)
...
Итого: 250.3
'''


class Clothes:
    def __init__(self):
        pass

    #декоратор
    @property
    def cloth_size(self):
        pass

    def get_size(self):
        pass



class Suit(Clothes):
    def __init__(self,height):
        self.height=height

    @property
    def cloth_size(self):
        return 2*self.height+0.3
    #2 * height + 0.3

    def __str__(self):
        return f'{self.cloth_size:.2f} - {self.__class__.__name__} (height:{self.height})'

class Coat(Clothes):
    # size / 6.5 + 0.5
    def __init__(self,size):
        self.size=size

    @property
    def cloth_size(self):
        return 2 * self.size / 6.5 + 0.5

    def __str__(self):
        return f'{self.cloth_size:.2f} - {self.__class__.__name__} (height:{self.size})'




def clothes_list():
    import random
    return [random.choice([Coat(random.randint(40,50)),Suit(random.randint(40,50))]) for i in range(10)]

for i in clothes_list():
    print(i)


