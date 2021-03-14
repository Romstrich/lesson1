'''
адание 1. Функция-генератор rand_nums
Написать функцию-генератор rand_nums, генерирующую N
 случайных целых чисел в диапазоне 1 до 100 (включительно).
  Количество чисел N, которое выдаст генератор передается в функцию через параметр.

'''
from random import randint

def rand_nums(nom):
    '''
    генератор случайных чисел от  1  до 100
    '''
    for i in range(nom):
        yield randint(1,100)

if __name__=='__main__':
    num=int(input('сколько чисел?  _'))
    rand_x=rand_nums(num)
    for i in range(num):
        print(next(rand_x))