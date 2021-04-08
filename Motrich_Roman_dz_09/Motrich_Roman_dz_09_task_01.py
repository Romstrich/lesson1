'''
Создать класс TrafficLight (светофор).
определить у него один приватный атрибут
color (цвет) и метод get_current_signal()
(получить текущий цвет);
после создания экземпляра светофора, он
запускает режим смены сигналов с разной
длительностью: красный (3 сек), жёлтый
(1 сек), зелёный (3 сек);
переключение идет циклично в порядке
красный-жетлый-зеленый-красный-жетлый-зеленый-красный-...
проверить переключение режимов работы
светофора, опрашивая в цикле текущее
состояние светофора с интервалом 0.5 секунды,
используя метод get_current_signal().
'''
from datetime import datetime,timedelta
from time import sleep

class TrafficLight:
    __color = None
    __color_types = (['red', 3], ['yellow', 1], ['green', 3])

    def __init__(self):
        self.set_color('red')
        self.time_start=datetime.now()
        self.cycle_time=sum(x[1] for x in self.__color_types)
        print(self.cycle_time)

    def set_color(self,color):
        self.__color=color

    def get_current_signal(self):
        diff=(datetime.now()-self.time_start).total_seconds()
        shift=diff%self.cycle_time
        print(shift,end=' ')
        index=0
        while shift>self.__color_types[index][1]:
            print(index,shift)
            shift-=self.__color_types[index][1]
            index+=1
        self.__color=self.__color_types[index][0]
        return self.__color

road_light=TrafficLight()
for i in range(60):
    print(road_light.get_current_signal())
    sleep(0.5)