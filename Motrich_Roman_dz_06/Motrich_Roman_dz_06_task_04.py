'''
4. * (вместо 3) Решить задачу 3 для ситуации, когда
 объём данных в файлах превышает объём ОЗУ (разумеется,
  не нужно реально создавать такие большие файлы, это
  просто задел на будущее проекта). Также реализовать
  парсинг данных из файлов - получить отдельно фамилию,
  имя и отчество для пользователей и название каждого
  хобби: преобразовать в какой-нибудь контейнерный тип
  (список, кортеж, множество, словарь). Обосновать выбор
  типа. Подумать, какие могут возникнуть проблемы при
  парсинге. В словаре должны храниться данные, полученные
  в результате парсинга.
'''

import pickle

users_f=open('users.csv', 'r',encoding='utf-8')
hobby_f=open('hobby.csv', 'r',encoding='utf-8')

with open('save_u_h_4.csv','bw') as u_h_file:
    while True:
        u_line=users_f.readline().strip()
        if not u_line:
            if hobby_f.readline():
                users_f.close()
                hobby_f.close()
                u_h_file.close()
                exit(1)
            else:
                pass
            break
        else:
            h_line=hobby_f.readline()
            if not h_line:
                h_line=None
            else:
                h_line=h_line.strip().split(',')
            file_out_dict={'user':u_line.split(','),'hobby':h_line}

            print(file_out_dict)
            pickle.dump((u_line,h_line),u_h_file)
users_f.close()
hobby_f.close()
#выбран был словарь по пользователю  и хобби. тк. потом их можнобудет по отдельности достать(я так полагаю)
