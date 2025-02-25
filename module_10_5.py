import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


filenames = [f'D:/proj/pythonProjectUrban/module_10./file {number}.txt' for number in range(1, 5)]

# линейный вызов
start = datetime.datetime.now()
for file in filenames:
    read_info(file)
end = datetime.datetime.now()
print(f'{end - start} (линейный)')

# Многопроцессный вызов
if __name__=='__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'{end - start} (многопроцессный)')

=>
0:00:14.242436 (линейный)
0:00:07.211430 (многопроцессный)
