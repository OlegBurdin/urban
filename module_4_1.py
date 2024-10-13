import math
from math import inf
def divide(first, second):
    if second == 0:
        return (math.inf)
    else:
        return (first / second)

def divide(first, second):
    if second == 0:
       return ('Ошибка')
    else:
       return (first/second)


from fake_math import divide as div_1
from true_math import divide as div_2

result1 = div_1(69, 3)
result2 = div_1(3, 0)
result3 = div_2(49, 7)
result4 = div_2(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)

>
23.0
Ошибка
7.0
inf
