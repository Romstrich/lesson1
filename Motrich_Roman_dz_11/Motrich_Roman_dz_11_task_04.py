'''
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс
«Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер,
сканер, ксерокс). В базовом классе определите параметры,
общие для приведённых типов. В классах-наследниках
реализуйте параметры, уникальные для каждого типа оргтехники.
'''


class Storehouse:
    def __init__(self):
        pass

class OfficeEquipment:
    def __init__(self,name,coast):
        OfficeEquipment.name=name
        OfficeEquipment.coast=coast

class Scanner(OfficeEquipment):
    def __init__(self,name,coast,formats):
        OfficeEquipment.__init__(self,name,coast)
        Scanner.formats=formats

class Printer(OfficeEquipment):
    def __init__(self,name,coast,page_per_minute):
        OfficeEquipment.__init__(self,name,coast)
        self.page_per_minute=page_per_minute

class Copeer(OfficeEquipment):#, Scanner):#, Printer):
    def __init__(self,name,coast,page_per_minute,formats):
        OfficeEquipment.__init__(self,name,coast)
        self.page_per_minute=page_per_minute
        self.formats=formats

    def __str__(self):
        return  f'{self.name}\n{self.coast}\n{self.page_per_minute}\n{self.formats} '

s=Scanner('scaner-1',900,8)
c=Copeer('copy',200,60,['A4','A5'])
print(c)