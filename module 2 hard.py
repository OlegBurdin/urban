n = int(input('Введите число: '))
for i in range (1,n):
    for j in range (1,n):
        if i != j:
            if n % (i + j) == 0:
                print(i,j)