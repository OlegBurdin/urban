import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        counter = 100
        days = 0
        while counter:
            time.sleep(1)
            counter -= self.power
            days += 1
            print(f'{self.name} сражается {days} дней (дня) , осталось {counter} воинов')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все, битвы закончились!')
=>
Sir Lancelot, на нас напали!
Sir Galahad, на нас напали!
Sir Lancelot сражается 1 дней (дня) , осталось 90 воинов
Sir Galahad сражается 1 дней (дня) , осталось 80 воинов
Sir Galahad сражается 2 дней (дня) , осталось 60 воиновSir Lancelot сражается 2 дней (дня) , осталось 80 воинов

Sir Galahad сражается 3 дней (дня) , осталось 40 воинов
Sir Lancelot сражается 3 дней (дня) , осталось 70 воинов
Sir Galahad сражается 4 дней (дня) , осталось 20 воинов
Sir Lancelot сражается 4 дней (дня) , осталось 60 воинов
Sir Galahad сражается 5 дней (дня) , осталось 0 воинов
Sir Lancelot сражается 5 дней (дня) , осталось 50 воинов
Sir Galahad одержал победу спустя 5 дней(дня)!
Sir Lancelot сражается 6 дней (дня) , осталось 40 воинов
Sir Lancelot сражается 7 дней (дня) , осталось 30 воинов
Sir Lancelot сражается 8 дней (дня) , осталось 20 воинов
Sir Lancelot сражается 9 дней (дня) , осталось 10 воинов
Sir Lancelot сражается 10 дней (дня) , осталось 0 воинов
Sir Lancelot одержал победу спустя 10 дней(дня)!
Все, битвы закончились!

Process finished with exit code 0
