def custom_write(file_name, strings):
    n = 0
    strings_positions = {}
    file_name ='test.txt'
    file = open(file_name,'w', encoding='utf-8')
    for string in strings:
        tell = file.tell()
        n += 1
        file.write(string + '\n')
        strings_positions.update({(n, tell): string})
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
=>
D:\proj\pythonProject4\.venv\Scripts\python.exe D:\proj\pythonProject4\module_7_2.py 
((1, 0), 'Text for tell.')
((2, 16), 'Используйте кодировку utf-8.')
((3, 66), 'Because there are 2 languages!')
((4, 98), 'Спасибо!')

Process finished with exit code 0
