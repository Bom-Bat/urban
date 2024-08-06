class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weigt = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weigt}, {self.category}'


class Shop():
    __file_name = 'products.txt'
    file = open(__file_name, 'a')
    file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        file = open(self.__file_name, 'r')
        pr_str = file.read()
        for i in products:
            if i.name not in pr_str:
                file = open(self.__file_name, 'a')
                file.write(f'{i.name}, {i.weigt}, {i.category}\n')
                file = open(self.__file_name, 'r')
                pr_str = file.read()
            else:
                print(f'Продукт {i.name} уже есть в магазине')
            file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
