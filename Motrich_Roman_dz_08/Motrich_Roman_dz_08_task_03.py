'''
3. Написать декоратор для логирования типов
позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

 a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные
о каждом через запятую; можете ли вы вывести тип значения
функции? Сможете ли решить задачу для именованных
аргументов? Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции, например, в виде:
 a = calc_cube(5)
calc_cube(5: <class 'int'>)
'''


def type_logger(func):
    def in_func(*args, **kwargs):
        print('Передана функция:', func.__name__,end='(')
        for a in args:
            print(a, ':', type(a), end=',')

        for k in kwargs:
            print(k, ':',type(k), end=',')
        print(')\nРезультат:', func(*args, **kwargs))

    return in_func


@type_logger
def calc_cube(x,*eny_parameters,**my_kwargs):
    return x ** 3


calc_cube(9,46,'dsd',(4,5,6,7,8),cars=['shkoda','toyoda'],vech1='stels',vech2='stern')
