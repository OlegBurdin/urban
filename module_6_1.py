class Animal:
    fed = False # накормленный
    alive = True  # живой
    def __init__(self, name):
        self.name = name # индивидуальное название каждого животного.

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
class Plant:
    edible = False  # съедобность
    def __init__(self, name):
        self.name = name # индивидуальное название каждого растения

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
=>
D:\proj\pythonProject4\.venv\Scripts\python.exe D:\proj\pythonProject4\module_6_1.py 
Волк с Уолл-Стрит
Цветик семицветик
True
False
Волк с Уолл-Стрит не стал есть Цветик семицветик
Хатико съел Заводной апельсин
False
True

Process finished with exit code 0

 
