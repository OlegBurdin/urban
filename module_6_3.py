import random
class Animal: # класс описывающий животных.
    live = True
    sound = None # звук(изначально отсутствует)
    _DEGREE_OF_DANGER = 0 # степень опасности существа
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):

        if dz < 0:
            print("It's too deep, i can't dive")

        else:
            self._cords = [self.speed * dx, self.speed * dy, self.speed * dz]

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful")
        else:
            print("Be careful, i'm attacking you 0_0")
    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True # наличие клюва
    def lay_eggs(self):
        random_integer = random.randint(1, 4)
        print(f"Here are(is) {random_integer} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self.dz = dz
        self._cords[2] = int(abs(dz) * self.speed * 0.5 - self._cords[2])


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"


print(Duckbill.mro())
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

=>
D:\proj\pythonProject4\.venv\Scripts\python.exe D:\proj\pythonProject4\module_6_3.py 
[<class '__main__.Duckbill'>, <class '__main__.Bird'>, <class '__main__.PoisonousAnimal'>, <class '__main__.AquaticAnimal'>, <class '__main__.Animal'>, <class 'object'>]
True
True
Click-click-click
Be careful, i'm attacking you 0_0
X: 10, Y: 20, Z: 30
X: 10, Y: 20, Z: 0
Here are(is) 2 eggs for you

Process finished with exit code 0

