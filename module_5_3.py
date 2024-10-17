class House:
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

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

=>
D:\proj\pythonProject4\.venv\Scripts\python.exe D:\proj\pythonProject4\module_5_3.py 
Название: ЖК Эльбрус, кол-во этажей: 10.
Название: ЖК Акация, кол-во этажей: 20.
False
Название: ЖК Эльбрус, кол-во этажей: 20.
True
Название: ЖК Эльбрус, кол-во этажей: 30.
Название: ЖК Акация, кол-во этажей: 30.
False
True
False
True
False

Process finished with exit code 0
