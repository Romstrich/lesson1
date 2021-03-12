'''Задание 2. Курс Валюты
Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
Код валюты может быть в произвольном регистре.
Функция должна возвращать результат числового типа, например float.
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
http://www.cbr.ru/scripts/XML_daily.asp.

Выведите на экран курсы для доллара и евро, используя написанную функцию.

Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере, посмотреть содержимое ответа.
'''
import requests

def import_curency_rate(currency_code):
    response=requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content=response.content.decode(encoding="windows-1251").split('<Valute ID=')
    #meta=content[0] #заготовка под дату
    #print(meta)
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

    currency_value = float('.'.join(conteiner['Value'].split(','))[:-2])

    return currency_value


print(import_curency_rate('KRW'))


