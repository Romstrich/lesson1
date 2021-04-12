'''
2. Создайте собственный класс-исключение,
обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с
ошибкой.
'''

class MyError(Exception):
    pass

class MyZeroDevision(MyError):
    def __init__(self):
        try:
            print('делить на ноль нельзя')
        except ZeroDivisionError as e:
            print('делить на ноль нельзя')
        else:
            pass

a = int(input('Введите делимое '))
b = int(input('Введите делитель '))
c=0
try:
    if b==0:
        raise MyZeroDevision
    else:
        c=a/b
except MyZeroDevision:
    # print('делить на ноль нельзя')
    pass
else:
    print(f'результат теления: {c}')
finally:
    print('работаю дальше')