def all_variants(text):
    for x in range(len(text)):
        for y in range(len(text) - x):
            yield text[y:y + x + 1]


a = all_variants("abc")
for i in a:
    print(i)
=>
a
b
c
ab
bc
abc

Process finished with exit code 0
