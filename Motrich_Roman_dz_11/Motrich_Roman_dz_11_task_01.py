'''
1. Реализовать класс «Дата», функция-конструктор которого
должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором
@classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором
@staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной
структуры на реальных данных.
'''


class Data:
    data_str = None

    def __init__(self, in_data):
        self.data_str=in_data

    @classmethod
    def get_data_numbers(cls, data_str):
        import re
        try:
            nomber = re.compile(r"^([0-3][0-9])[\-][01][0-9][\-][12][0-9][0-9][0-9]$", re.S)
            month = re.compile(r"^[0-3][0-9][\-]([01][0-9])[\-][12][0-9][0-9][0-9]$", re.S)
            year = re.compile(r"^[0-3][0-9][\-][01][0-9][\-]([12][0-9][0-9][0-9])$", re.S)
            return {'nomber': nomber.findall(data_str)[0], 'month': month.findall(data_str)[0],
                    'year': year.findall(data_str)[0]}
        except BaseException as e:
            print('Ошибка')
            return None


    @staticmethod
    def data_valid(data_sep) -> object:
        valid = False

        try:
            if int(data_sep['nomber']) < 32 and int(data_sep['nomber']) > 0:
                print(data_sep['nomber'])
                if int(data_sep['month']) < 13 and int(data_sep['month']) > 0:
                    print(data_sep['month'])
                    if int(data_sep['year']) > 0:
                        print(data_sep['year'])
                        valid = True
        except BaseException as e:
            print('Ошибочка')
        else:
            pass
        finally:
            return valid

    def __str__(self):
        return self.data_str




my_data=Data('12-03-2201')
print(my_data)
print(my_data.get_data_numbers(my_data.data_str))
if my_data.data_valid(my_data.get_data_numbers(my_data.data_str)):
    print('дата верная')
else:
    print('дата не верная')


