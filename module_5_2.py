
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

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))

>
D:\proj\pythonProject4\.venv\Scripts\python.exe D:\proj\pythonProject4\module_5_2.py 
Название: ЖК Эльбрус, кол-во этажей: 10.
Название: ЖК Акация, кол-во этажей: 20.
10
20

Process finished with exit code 0
