'''
Не используя библиотеки для парсинга, распарсить
 (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/
Common%20Data%20Formats/nginx_logs/nginx_logs) —
 получить список кортежей вида: (<remote_addr>,
  <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
'''

'''
план:
втупую:открыл, парс, записал
модерн:запись списков, таак что json сойдёт
'''
import json

f1=open('nginx_logs.txt','r')
f2=open('parsed_logs.txt','w')
while True:
    line=f1.readline().split()
    if not line:
        break
    print(line[0],line[5][1:],line[6])
    print(line[0], line[5][1:], line[6])
    json.dump([line[0],line[5][1:],line[6]],f2)
f1.close()
f2.close()