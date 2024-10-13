
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(item):
    add = 0

    def calculate(item):
        nonlocal add
        if isinstance(item, int):
            add += item
        elif isinstance(item, str):
            add += len(item)
        elif isinstance(item, (set, tuple, list)):
            for i in item:
                add += calculate_structure_sum(i)
        elif isinstance(item, dict):
            for key, value in item.items():
                add += calculate_structure_sum(key)
                add += calculate_structure_sum(value)

    calculate(item)
    return add

resulte = calculate_structure_sum(data_structure)
print(resulte)
