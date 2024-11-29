def add_everything_up(a,b):
    try:
        answer = a + b
        return answer
    except TypeError:
        return f'{a}, {b}'

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
=>
123.456, строка
яблоко, 4215
130.456

Process finished with exit code 0
