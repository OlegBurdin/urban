team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

print('В команде Мастера кода участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num,team2_num))
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {} с'.format(team1_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: победа команды {challenge_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')

print('')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(result)
=>
D:\proj\pythonProject4\.venv\Scripts\python.exe "C:\Users\Asus Lap-Top\Downloads\module_7_4.py" 
В команде Мастера кода участников: 5!
Итого сегодня в командах участников: 5 и 6!
Команда Волшебники данных решила задач: 42!
Волшебники данных решили задачи за 1552.512 с
Команды решили 40 и 42 задач.
Результат битвы: победа команды Победа команды Волшебники данных!!
Сегодня было решено 82 задач, в среднем по 45.2 секунды на задачу!.

Победа команды Волшебники Данных!

Process finished with exit code 0
