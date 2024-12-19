import threading
import time
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            word = f'Какое-то слово № {i}\n'
            file.write(word)
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

hello = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
goodbye = time.time()
print(f'Работа потоков: {goodbye - hello:.2f}')

threads = []

threads.append(threading.Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(threading.Thread(target=write_words, args=(30, 'example6.txt')))
threads.append(threading.Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(threading.Thread(target=write_words, args=(100, 'example8.txt')))

start_time = time.time()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()

print(f'Работа потоков: {end_time - start_time:.2f}')
=>
Завершилась запись в файл example1.txt
Завершилась запись в файл example2.txt
Завершилась запись в файл example3.txt
Завершилась запись в файл example4.txt
Работа потоков: 34.22
Завершилась запись в файл example5.txt
Завершилась запись в файл example6.txt
Завершилась запись в файл example8.txt
Завершилась запись в файл example7.txt
Работа потоков: 20.14
