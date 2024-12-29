import threading
import time
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):

        for _ in range(100):
            random_number = random.randint(50, 500)
            self.balance += random_number
            print(f'Пополнение: {random_number}. Баланс: {self.balance}.')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):

        for _ in range(100):
            random_number = random.randint(50, 500)
            print(f'Запрос на {random_number}')

            if random_number <= self.balance:
                self.balance -= random_number
                print(f'Снятие: {random_number}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
 =>
Пополнение: 57. Баланс: 57.
Запрос на 166
Запрос отклонён, недостаточно средств
Пополнение: 277. Баланс: 334.
Запрос на 471
Запрос отклонён, недостаточно средств
Пополнение: 495. Баланс: 829.
Запрос на 205
Снятие: 205. Баланс: 624.
Пополнение: 436. Баланс: 1060.
...
Запрос на 358
Запрос отклонён, недостаточно средствПополнение: 76. Баланс: 362.

Запрос на 439
Пополнение: 493. Баланс: 855.
Снятие: 439. Баланс: 416.
Запрос на 374
Снятие: 374. Баланс: 42.
Итоговый баланс: 42

Process finished with exit code 0
