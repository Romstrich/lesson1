'''
4. Написать скрипт, который выводит статистику
для заданной папки в виде словаря, в котором ключи — верхняя
граница размера файла (пусть будет кратна 10), а значения —
общее количество файлов (в том числе и в подпапках), размер
которых не превышает этой границы, но больше предыдущей
(начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
'''

import os,shutil

def files_sizes(dir_name='007_some_data'):
    return_dict={}
    try:
        for file in os.listdir(dir_name):
            file_size=os.stat(dir_name+'\\'+file).st_size
            file_size=10**(len(str(file_size))+1)
            if return_dict.get(file_size)==None:
                return_dict.setdefault(file_size,1)
            else:
                return_dict[file_size]+=1

        return return_dict
    except BaseException as error:
        print('Возникла некоторая ошибка, возращаю её объект')
        return error

print(files_sizes())