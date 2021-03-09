'''2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы. Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"
'''
def num_translate_adv(my_num):
    num_dict={'zero':'нуль','one':'один','two':'два','three':'три'\
              ,'four':'четыре','five':'пять','six':'шесть','seven':'семь'\
              ,'eight':'восемь','nine':'девять','ten':'десять'}
    if num_dict.get(my_num.lower())!=None:
        # num_dict.get(my_num.lower())
        if my_num.islower():
            return num_dict.get(my_num.lower())
        elif my_num.istitle():
            return num_dict.get(my_num.lower()).capitalize()
        else:
            return None
    else:
        return None

while True:
    my_num=input('Введите числительное на английском\nот 0 до 10: ')#это не та переменная, что в функции=)
    if num_translate_adv(my_num)!=None:
        print('"{0}" переводится, как "{1}"'.format(my_num,num_translate_adv(my_num)))
    else:
        break