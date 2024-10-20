class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for new_floor in range(new_floor + 1):
                if new_floor < 1:
                    continue
                print(new_floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}.'

    def __eq__(self, other):
        if isinstance(other.number_of_floors, int) or isinstance(other.number_of_floors, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int) or isinstance(value, House):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        if isinstance(value, int) or isinstance(value, House):
            self.number_of_floors += value
            return self

    def __iadd__(self, value):
        if isinstance(value, int) or isinstance(value, House):
            self.number_of_floors += value
            return self

    def __del__(self):
      print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)

=>
D:\proj\pythonProject4\.venv\Scripts\python.exe D:\proj\pythonProject4\module_5_4.py 
['ЖК Эльбрус']
['ЖК Эльбрус', 'ЖК Акация']
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Акация снесён, но он останется в истории
ЖК Матрёшки снесён, но он останется в истории
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Эльбрус снесён, но он останется в истории

Process finished with exit code 0
