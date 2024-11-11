class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner # владелец транспорта.(владелец может меняться)
        self.__model = __model # модель(марка) транспорта.(мы не можем менять название модели)
        self.__engine_power = __engine_power # мощность двигателя.(мы не можем менять мощность двигателя самостоятельно)
        self.__color = __color # название цвета.


    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.lower()
        else:
            print (f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 # (в седан может поместиться только 5 пассажиров)
    pass




vehicle1 = Vehicle('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

=>
D:\proj\pythonProject4\.venv\Scripts\python.exe D:\proj\pythonProject4\module_6_2.py 
Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: blue
Владелец: Fedos
Нельзя сменить цвет на Pink
Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: black
Владелец: Vasyok

Process finished with exit code 0
