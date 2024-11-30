def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        result, incorrect_data = personal_sum(numbers)
        if incorrect_data > 0:
            for i in numbers:
                if not isinstance(i, (int, float)):
                    print(f'Некорректный тип данных для подсчёта суммы - {i}')
        return result / len(numbers)
    except ZeroDivisionError:
        print("Ошибка: коллекция numbers пуста.")
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных.")
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print('')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print('')
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print('')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
=>
Некорректный тип данных для подсчёта суммы - 1
Некорректный тип данных для подсчёта суммы - ,
Некорректный тип данных для подсчёта суммы -  
Некорректный тип данных для подсчёта суммы - 2
Некорректный тип данных для подсчёта суммы - ,
Некорректный тип данных для подсчёта суммы -  
Некорректный тип данных для подсчёта суммы - 3
Результат 1: 0.0

Некорректный тип данных для подсчёта суммы - Строка
Некорректный тип данных для подсчёта суммы - Ещё Строка
Результат 2: 1.0

В numbers записан некорректный тип данных.
Результат 3: None

Результат 4: 26.5

Process finished with exit code 0
