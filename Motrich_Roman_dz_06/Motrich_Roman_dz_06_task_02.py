'''2. * (вместо 1) Найти IP адрес спамера и количество
 отправленных им запросов по данным файла логов из
  предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех
 запросов; код должен работать даже с файлами, размер
  которых превышает объем ОЗУ компьютера.'''

import json

spam={}
f1=open('nginx_logs.txt','r')
f2=open('parsed_logs.txt','w')
while True:
    line=f1.readline().split()
    if not line:
        break
    #print(line[0],line[5][1:],line[6])
    json.dump([line[0],line[5][1:],line[6]],f2)
    if spam.get(line[0])!=None:
        spam[line[0]]+=1
    else:
        spam[line[0]]=1
f1.close()
f2.close()
list1=list(map(lambda x,y:[x,y],spam.values(),spam.keys()))
list1=sorted(list1,reverse=True)[0]
print(f'НАШ СПАММЕР:{list1[1]}\nОбратился к сайту:{list1[0]} раз')