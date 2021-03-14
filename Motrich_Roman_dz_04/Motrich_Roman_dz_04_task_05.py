'''
Задание 5. * Вызов с командной строки
Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли,
а коды валют ему дожны передавать через аргументы командной строки (там может быть один или несколько кодов).
Вывод курсов сделать в том же порядке, что присланные аргументы
Например:

python task5.py USD EUR
USD 75.18, 2020-09-05
EUR 80.35, 2020-09-05

Ввод кодов с ЗАГЛАВНЫМИ БУКВАМИ через пробел латиницей
'''

from utils import print_curency_rate, import_curency_rate
import sys

if __name__=='__main__':
    if len(sys.argv)>=2:
        for i in range(len(sys.argv)-1):
            print_curency_rate(import_curency_rate(sys.argv[i+1]))
    else:
        print(__doc__)
        print('Введите верно параметры')
else:
    print('not main')

# curency=input('Введите код валюты заглавными буквами: ')
# print_curency_rate(import_curency_rate(curency))

