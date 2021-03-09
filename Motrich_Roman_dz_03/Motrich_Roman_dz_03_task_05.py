'''
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех слов,
 взятых из трёх списков (по одному слову из каждого списка):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг,
 разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно
использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

'''
from random import shuffle, choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


# вариант-1
def get_jokes(j_nomber=2, re_play=True):
    '''
    get_jokes(j_nomber=2, re_play=True)
    :param j_nomber:  количество шуток (по умолчанию 2)
    :param re_play: повтор слов (по умолчанию включён)
    :return: возвращает шутки из случайно выбраных слов трёх
    указанных списков
    Примечание: в режиме без повтора, при превышении требуемым
    количеством шуток реально возможного, на экран выводится
    предупреждение. При этом функция возвращает максимально
    возможное кольчество шуток.
    '''
    j_list = []
    if re_play == True:
        for i in range(j_nomber):
            j_list.append(' '.join([choice(nouns), choice(adverbs), choice(adjectives)]))
    elif re_play == False:
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        # Выявим минимальный по длине список и сравним его с заданым количеством смешков
        if j_nomber <= min(len(nouns), len(adverbs), len(adjectives)):
            for i in range(j_nomber):
                j_list.append(' '.join([nouns.pop(), adverbs.pop(), adjectives.pop()]))
        else:
            print('заданое количество больше возможных вариантов!!!'
                  '\n',j_nomber,'>',min(len(nouns), len(adverbs), len(adjectives)))
            for i in range(min(len(nouns), len(adverbs), len(adjectives))):
                j_list.append(' '.join([nouns.pop(), adverbs.pop(), adjectives.pop()]))

    return j_list


print(get_jokes.__doc__)
while True:
    n_jokes=int(input('Задайте количество шуток для генератора, для выхода - 0\n'))
    if n_jokes > 0:
        re_play=bool(input('задайте повтора (True, False)\n'))
        print(get_jokes(n_jokes, re_play), end='\n\n')
    else:
        print('Выход')
        break

