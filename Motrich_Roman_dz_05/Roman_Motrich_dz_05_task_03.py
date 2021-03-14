'''
Задание 3. Генератор объединения двух списков
Есть два списка:

```
tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
]
klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
```
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:

('Иван', '9А')
('Анастасия', '7В')
...

Количество генерируемых кортежей должно быть равно длине
 списка tutors. Если в списке klasses меньше элементов,
 чем в списке tutors, необходимо вывести последние кортежи
  в виде: (<tutor>, None), например:
```('Станислав', None)```
Доказать, что вы создали именно генератор. Проверить его
 работу вплоть до истощения. Подумать, в каких ситуациях
  генератор даст эффект.
'''

tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена','Катя','Боря','Света','Егор'
        ]
klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
        ]

def school_gen(tut,klass):
    for i in range(len (tut)):
        if i+1>len(klass):
            yield (tut[i], None)
        else:
            yield (tut[i],klass[i])


s_g=school_gen(tutors,klasses)
for i in range(len(tutors)):
    print(next(s_g))