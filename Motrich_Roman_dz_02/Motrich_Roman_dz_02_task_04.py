#-*-coding:utf-8-*-
'''
Задание 4
Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на экран фразы вида: 'Привет, Игорь!
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?
'''
office_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',\
             'директор аэлита','Секретарь сНеЖаНа', 'курьер срочной доставки пЕтя', 'программист ваСЯ']
men_list = []
input('Вариант со списком. Нажмите Enter.\n\t----------')
for k in office_list:
    #temp_name = ''.join(k.split(' ')[-1:]).capitalize()
    men_list.append('Привет, '+''.join(k.split(' ')[-1:]).capitalize()+'!')
for i in men_list:
    print(i)
input('Вариант без списка. Нажмите Enter.\n\t----------')
for k in office_list:
    print('Привет, '+''.join(k.split(' ')[-1:]).capitalize()+'!')
