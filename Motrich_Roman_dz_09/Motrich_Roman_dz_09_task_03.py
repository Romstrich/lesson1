'''
3. Реализовать базовый класс Employee (сотрудник).
определить атрибуты: name (имя), surname (фамилия),
которые должны передаваться при создании экземпляра Employee;
создать класс Position (должность) с аттрибутами employee
(сотрудник/Employee), position (должность/str),
income (вознаграждение/dict) - атрибуты также
задаются при создании экземпляра класса;
последний атрибут должен быть защищённым и ссылаться
на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus};
в классе Position реализовать методы получения полного
имени сотрудника get_full_name() и дохода с учётом
премии get_total_income() (wage + bonus);
проверить работу примера на реальных данных: создать
экземпляры классов Employee, Position, вывести на
экран имя сотрудника, его должность и вознаграждение
сотрудника, используя методы класса Position.
'''


class Employee:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Position:
    __income = {"wage":None, "bonus":None};
    def __init__(self, position, employee, wage,bonus):
        self.employee = employee
        self.position = position
        self.__income['wage']=wage
        self.__income['bonus'] = bonus

    def get_full_name(self):
        return ' '.join([self.employee.name, self.employee.surname])

    def get_total_income(self):
        return self.__income["wage"]+self.__income["bonus"]

    def get_position(self):
        return self.position

petrov=Employee('Вася','Петров')
petrov_pos=Position('деятель',petrov,100000,30000)
print(petrov_pos.get_position())
print(petrov_pos.get_full_name())
print(petrov_pos.get_total_income())
