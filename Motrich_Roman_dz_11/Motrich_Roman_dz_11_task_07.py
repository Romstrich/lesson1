'''
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число». Реализуйте
перегрузку методов сложения и умножения комплексных
чисел. Проверьте работу проекта. Для этого создаёте
экземпляры класса (комплексные числа), выполните
сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''


class Complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return f'{self.a}+{self.b}i'

    def __add__(self, other):
        return Complex(self.a+other.a,self.b+other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complex((self.a*other.a-self.b*other.b),(self.a*other.b+self.b*other.a))


k=Complex(3,6)
print(k)
k1=Complex(5,2)
print(k1)
k2=k+k1
print(k2)
k2=k*k1
print(k2)