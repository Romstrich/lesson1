'''
2. * (вместо 1) Написать скрипт, создающий из config.yaml
стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами,
его можно создать в любом текстовом редакторе «руками»
(не программно); предусмотреть возможные исключительные
ситуации, библиотеки использовать нельзя.
'''
import Motrich_Roman_dz_07_task_01 as my_module
import os

def start_project2(path_list):
    for i in path_list:
        if '.' in i:
            if os.path.isfile(i):
                print(i,'-существующий файл. оставляем.')
            else:
                print(i,'-файл отсутствует...',end=' ')
                f_tmp=open(i,'w')
                f_tmp.close()
                print(i,'создан')
        else:
            if os.path.exists(''.join(i.split())):
                print(''.join(i.split()),'-каталог существует. оставляем.')
            else:
                print(''.join(i.split()), '-каталог отсутствует...',end=' ')
                os.makedirs(''.join(i.split()))
                print(''.join(i.split()), 'создан')


if __name__=='__main__':
    start_project2(my_module.load_config('config.yaml'))
