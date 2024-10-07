#def test_func(*params):
#    print(params)
#   print("Тип:", type(params))
#    print("Аргумент:", params)

#test_func(1, 2, 3, 'string')

#def summator(txt, *values, type = "sum"):
 #   s = 0
  #  for i in values:
   #     s += i
    #return f'{txt}{s} {type}'

#print(summator("Сумма чисел: ", 2, 3, 4, type="summator"))

#def info (value, *types, name_author="den", **values):
 #   print("Тип:", type(values))
  #  print("Аргумент:", values)
   # for key, value in values.items():
    #    print(key, value)
    #print(types)

#info("пример использования параметров всех типов",123, name="Denis", course="Urban")

#def my_sum(n, *args, txt = "Сумма чисел"):
 #   s = 0
  #  for i in range(len(args)):
   #     s += args[i] ** n
    #print(txt + ":", s)


#my_sum(1, 1, 2, 3, 4, 5)
#my_sum(2, 2, 3, 4, 5, txt = "Сумма квадратов")

def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)