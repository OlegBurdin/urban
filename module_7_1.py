# создается файл products.txt
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file1 = open(self.__file_name, 'r')
        products = file1.read()
        file1.close()
        return products

    def add(self, *products):
        file = open(self.__file_name, 'r+')
        for i in products:
            if str(i) in self.get_products():
                print(f'Продукт {i} уже есть в магазине')
            else:
                file.write(str(i) + '\n')
        file.close()
=>

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
=>
D:\proj\pythonProject4\.venv\Scripts\python.exe D:\proj\pythonProject4\module_7_1.py 
Spaghetti, 3.4, Groceries
Продукт Potato, 50.5, Vegetables уже есть в магазине
Продукт Spaghetti, 3.4, Groceries уже есть в магазине
Продукт Potato, 5.5, Vegetables уже есть в магазине
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables


Process finished with exit code 0
