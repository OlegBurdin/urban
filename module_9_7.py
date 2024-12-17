def is_prime(fanc):
    def wrapper(a, b, c):
        num = fanc(a, b, c)
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            print('Простое')
        else:
            print('Составное')
        return num
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(5, 0,2)
print(result)
=>
Простое
7

Process finished with exit code 0
