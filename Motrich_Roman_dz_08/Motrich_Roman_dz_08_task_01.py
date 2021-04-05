'''1. Написать функцию email_parse(<email_address>),
которая при помощи регулярного выражения извлекает имя
пользователя и почтовый домен из email адреса и
возвращает их в виде словаря. Если адрес не валиден,
выбросить исключение ValueError. Пример:
email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в
адресе и постарайтесь учесть их в регулярном
выражении; имеет ли смысл в данном случае
использовать функцию re.compile()?
'''


def email_parse(email_address):
    import re
    correct_email=re.compile(r"^[\w.-]+@[\w-]+.[a-zA-Z]{2,6}$",re.I)
    print(correct_email.findall(email_address))
    if correct_email.findall(email_address)!=[]:
        user_name=re.compile(r"^([\w.-]+)",re.S)
        domain_name=re.compile(r"^[\w.-]+@([\w-]+.[\w]{2,6})$",re.I)
        return {'username': user_name.findall(email_address)[0], 'domain': domain_name.findall(email_address)[0]}
    else:
        raise ValueError('Некорректый e-mail!!!')



print(email_parse('вапап.t@fdss.dfdfp'))