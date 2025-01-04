from threading import Thread
from random import randint
from queue import Queue
from time import sleep

class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):  # обслуживание гостей
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f'{next_guest.name} вышел из очереди и сел(-а)  за стол номер {table.number}')



 #Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

=>
"C:\Users\Asus Lap-Top\AppData\Local\Programs\Python\Python312\python.exe" D:\proj\pythonProjectUrban\module_10\module_10_4.py 
Maria сел(-а) за стол номер 1
Oleg сел(-а) за стол номер 2
Vakhtang сел(-а) за стол номер 3
Sergey сел(-а) за стол номер 4
Darya сел(-а) за стол номер 5
Arman в очереди
Vitoria в очереди
Nikita в очереди
Galina в очереди
Pavel в очереди
Ilya в очереди
Alexandra в очереди
Maria покушал(-а) и ушёл(ушла)
Стол номер 1 свободен
Arman вышел из очереди и сел(-а)  за стол номер 1
Darya покушал(-а) и ушёл(ушла)
Стол номер 5 свободен
Vitoria вышел из очереди и сел(-а)  за стол номер 5
Oleg покушал(-а) и ушёл(ушла)
Стол номер 2 свободен
Nikita вышел из очереди и сел(-а)  за стол номер 2
Vitoria покушал(-а) и ушёл(ушла)
Стол номер 5 свободен
Galina вышел из очереди и сел(-а)  за стол номер 5
Vakhtang покушал(-а) и ушёл(ушла)
Стол номер 3 свободен
Pavel вышел из очереди и сел(-а)  за стол номер 3
Sergey покушал(-а) и ушёл(ушла)
Стол номер 4 свободен
Ilya вышел из очереди и сел(-а)  за стол номер 4
Arman покушал(-а) и ушёл(ушла)
Стол номер 1 свободен
Alexandra вышел из очереди и сел(-а)  за стол номер 1
Nikita покушал(-а) и ушёл(ушла)
Стол номер 2 свободен
Ilya покушал(-а) и ушёл(ушла)
Стол номер 4 свободен
Galina покушал(-а) и ушёл(ушла)
Стол номер 5 свободен
Alexandra покушал(-а) и ушёл(ушла)
Стол номер 1 свободен
Pavel покушал(-а) и ушёл(ушла)
Стол номер 3 свободен

Process finished with exit code 0
