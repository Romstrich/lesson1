'''
модуль к заданию 4
'''
import requests,datetime
from decimal import Decimal


def import_curency_rate(currency_code):
    '''
    :param currency_code: Нужен код валюты заглавными буквами
    :return: словарь с названием валюты и датой
    берёт с сайта ЦБ данные о валютах и выискивает нужную, чтобы понять,
    что это верно - возвращает дату с тогоже сайта
    '''
    response=requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content=response.content.decode(encoding="windows-1251").split('<Valute ID=')
    meta=content[0] #заготовка под дату
    found=0
    conteiner = {}
    for k in range(len(content)):

        content[k]=content[k].split('><')
        for i in range(len(content[k])):
            content[k][i] = content[k][i].split('>')
            content[k][i] = content[k][i][-1]
            content[k][i] = content[k][i].split('</')
        #print(content[k])#content[k])

        for i in content[k]:
            conteiner[i[-1]]=i[0]

        if conteiner.get('CharCode')==currency_code:
            found+=1
            break

    if found==0:
        return None

    currency_value = Decimal('.'.join(conteiner['Value'].split(',')))
    currency_value=currency_value.quantize(Decimal("1.00"))


    meta=meta.split()
    tmp_date=0
    #print(meta)
    for i in meta:
        if i.find('Date')!=-1:
            tmp_date=i.split('=')[-1]
            #print(tmp_date[1:-1])
            tmp_date=tmp_date[1:-1].split('.')
            #print(tmp_date)
            tmp_date=datetime.date(int(tmp_date[-1]),int(tmp_date[-2]),int(tmp_date[-3]))
    #print(tmp_date)
    return_dict={'code':currency_code,'value':currency_value,'date':tmp_date}
    return return_dict

def print_curency_rate(curr_dict):
    '''
    :param curr_dict: словарь
    :return: печатает в формате EUR 87.80, 2021-03-13
    '''
    if curr_dict!=None:
        print('{0} {1}, {2}'.format(curr_dict['code'],curr_dict['value'],curr_dict['date']))
    else:
        print('Неверный код. Неверные данные. Ошибка')




