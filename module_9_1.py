def apply_all_func(int_list, *functions):
    results = {}
    for fun in functions:
        results[fun.__name__] = fun(int_list)
    return results
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

=>
{'max': 20, 'min': 6}
{'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}

Process finished with exit code 0
