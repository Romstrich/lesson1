'''. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
в которых фамилия начинается с соответствующей буквы. Например:
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Сможете ли вы вернуть отсортированный по ключам словарь?
'''

def thesaurus_adv(*full_names):
    # Разделим по именам
    select_names=list(map(lambda x:x.split(),full_names))
    print(select_names)
    #спсиок букв фамилий
    last_name_liter=set(map(lambda x:x[1][0],select_names))
    print(last_name_liter)
    office_dict={}
    #office_dict=dict(map(lambda x,y:(x,y if y[1][0].upper()==x else 'pass') ,last_name_liter,select_names))#[['Кn','И'],['Hn','С'],['En','Аn']]))
    for i in select_names:
        if office_dict.get(i[1][0].upper())!=None:
            office_dict[i[1][0].upper()].append(i)
        else:
            office_dict[i[1][0]]=[i]
    for k in office_dict.keys():
        tmp_list=office_dict[k].copy()
        office_dict[k]={}
        print(tmp_list)
        for i in tmp_list:
            if office_dict[k].get(i[0][0].upper())!=None:
                print('found')
                office_dict[k][i[0][0].upper()].append(i)
            else:
                print('not found')
                office_dict[k][i[0][0].upper()]=[i]


        return office_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева","Павел Ильюшин"))