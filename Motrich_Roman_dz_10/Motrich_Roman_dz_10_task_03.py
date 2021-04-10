'''
3. Осуществить программу работы с органическими клетками,
состоящими из ячеек.
Необходимо создать класс «Клетка». В его конструкторе
инициализировать параметр, соответствующий количеству
ячеек клетки (целое число). В классе должны быть реализованы
методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Эти методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и округление до целого числа деления клеток,
соответственно.
    Сложение. Объединение двух клеток. При этом число ячеек общей клетки
должно равняться сумме ячеек исходных двух клеток.
    Вычитание. Участвуют две клетки. Операцию необходимо выполнять,
только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
    Умножение. Создаётся общая клетка из двух. Число ячеек общей
клетки — произведение количества ячеек этих двух клеток.
    Деление. Создаётся общая клетка из двух. Число ячеек общей клетки
определяется как целочисленное деление количества ячеек этих двух клеток.

Добавить к классу метод print(columns), распечатыващий на экране
звездочки рядами по columns звездочек в одном ряду в количестве
равном числу ячеек клетки.
Если ячеек на формирование ряда не хватает, то в последний ряд
записываются все оставшиеся.
Например, если в клетке 12 ячеек, а запросили напечатать по 5
звездочек в ряду, то на экране должно быть:

*****
*****
**
'''

class Cell:
    def __init__(self,units):
        self.units=units

    def __add__(self,cell2):
        return Cell(self.units+cell2.units)

    def __sub__(self,cell2):
        if self.units>cell2.units:
            return Cell(self.units-cell2.units)
        else:
            print('В таком порядке разница невозможна')

    def __mul__(self,cell2):
        return Cell(self.units * cell2.units)

    def __truediv__(self,cell2):
        return Cell(self.units % cell2.units)

    def __str__(self):
        return str(self.units)

    def print(self,columns):
        if columns>0:
            print(self.units//columns*(columns*'*'+'\n')+self.units%columns*'*')
        else: print(self.units*'*')

def revision():
    from random import randint
    a =Cell(randint(0, 30))
    b =Cell(randint(0, 30))
    coloumns=randint(0,10)
    print(f'колонок задано {coloumns}')
    print(a)
    a.print(coloumns)
    print(b)
    b.print(coloumns)
    for i in range(10):
        oper=randint(0,4)
        if oper == 0:
            c=a+b
            print('c=a+b, c.units=',c.units)
            c.print(coloumns)
        elif oper == 1:
            try:
                c = a - b
                print('c=a-b, c.units=', c.units)
                c.print(coloumns)
            except AttributeError as e:
                print('a-b Не возможно вычесть')
        elif oper == 1:
            c = a * b
            print('c=a*b, c.units=', c.units)
            c.print(coloumns)
        elif oper == 1:
            c = a + b
            print('c=a/b, c.units=', c.units)
            c.print(coloumns)
        if oper == 0:
            c=a+b
            print('c=a+b, c.units=',c.units)
            c.print(coloumns)
        elif oper == 4:
            try:
                c = b - a
                print('c=b-a, c.units=', c.units)
                c.print(coloumns)
            except AttributeError as e:
                print('b-a Не возможно вычесть')

revision()