'''
4. Написать декоратор с аргументом-функцией (callback),
позволяющий валидировать входные значения функции и
выбрасывать исключение ValueError, если что-то не так,
например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


a = calc_cube(5)
125
a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
'''



def val_checker(func,nomber):
    def check(*args, **kwargs):
        return args
    return check



def type_logger(func):
    def in_func(*args, **kwargs):
        print('Передана функция:', func.__name__,end='(')
        for a in args:
            print(a, ':', type(a), end=',')
        for k in kwargs:
            print(k, ':',type(k), end=',')
        print(')\nРезультат:', func(*args, **kwargs))
    return in_func

@val_checker
def calc_cube(x):
    return x ** 3

#calc_cube=val_checker(calc_cube)
print(calc_cube(11))