'''
 Есть два файла: в одном хранятся ФИО пользователей сайта,
 а в другом — данные об их хобби. Известно, что при
 хранении данных используется принцип: одна строка —
 один пользователь, разделитель между значениями —
 запятая.
 Написать код, загружающий данные из обоих файлов и
 формирующий из них словарь: ключи — ФИО, значения —
 данные о хобби. Сохранить словарь в файл. Проверить
 сохранённые данные. Если в файле, хранящем данные о хобби,
 меньше записей, чем в файле с ФИО, задаём в словаре
 значение None. Если наоборот — выходим из скрипта с
 кодом «1». При решении задачи считать, что объём
 данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
'''
#раз ОЗУ в нашем распоряжении, можем использовать словарь на полную
#откроем и закроем оба два файла
import pickle

users_f=open('users.csv', 'r',encoding='utf-8')
hobby_f=open('hobby.csv', 'r',encoding='utf-8')
u_line=users_f.read().splitlines()
h_line=hobby_f.read().splitlines()
#сделаем проверку на длины
if len(u_line)>len(h_line):
    for i in range(len(u_line)-len(h_line)):
        h_line.append(None)
else:
    users_f.close()
    hobby_f.close()
    exit(1)
u_line=list(map(lambda x:' '.join(x.split(',')),u_line))
u_h_dict=dict(zip(u_line,h_line))
print(u_h_dict)
users_f.close()
hobby_f.close()

with open('save_u_h.csv','bw') as u_h_file:
    pickle.dump(u_h_dict,u_h_file)
