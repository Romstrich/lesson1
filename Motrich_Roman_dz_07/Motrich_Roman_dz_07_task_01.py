'''

1. Написать скрипт, создающий стартер (заготовку)
для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые
папки уже есть на диске (как быть?); как лучше
хранить конфигурацию этого стартера, чтобы в будущем
можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и
хранить данные о вложенных папках и файлах (добавлять детали)?
'''

import os

def load_config(config_name='config_1.cnf'):
        with open(config_name,'r',encoding='utf-8') as my_config:
            return list(map(lambda x:x.strip(),my_config.readlines()))

def start_project(path_list):
    for i in path_list:
        if os.path.exists(''.join(i.split())):
            print(''.join(i.split()),'существует')
        else:
            print(''.join(i.split()), 'будет создана')
            os.makedirs(''.join(i.split()))

if __name__ == '__main__':
    start_project(load_config())