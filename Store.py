class Store ():
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.items = {}  # Пустой список товаров

    def add_item(self,item_name,price):   # Метод для добавления товара

            self.items[item_name] = price
            print(f"Товар '{item_name}' добавлен в ассортимент магазина '{self.name}'.")

    def remove_item(self, item_name):    # Метод для удаления товара

        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента магазина '{self.name}'.")

        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте магазина '{self.name}'.")

    def get_price(self, item_name):     # Метод для извлечения цены

        return self.items.get(item_name, None)  # Возвращает None, если товар отсутствует

    def update_price(self, item_name, new_price):  # Метод для обновления цены товара.

        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена в магазине '{self.name}'.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте магазина '{self.name}'.")
    def __str__(self):     # Информация о магазине

        return f"Магазин: {self.name}, Адрес: {self.address}, Ассортимент: {self.items}"

# Создаем несколько объектов класса Store
store1 = Store("Магазин Фрукты", "ул. Ленина, 10")
store2 = Store("Супермаркет Овощи", "пр. Мира, 25")
store3 = Store("Пятерочка", "ул. Садовая, 5")

# Добавляем товары в магазины
store1.add_item("яблоки", 95)
store1.add_item("бананы", 120)
store2.add_item("морковь", 30)
store2.add_item("картофель", 40)
store3.add_item("молоко", 75)
store3.add_item("хлеб", 35)

# Обновляем цены на товары
store1.update_price("яблоки", 110)
store2.update_price("морковь", 45)

# Удаляем товары из ассортимента
store3.remove_item("молоко")

# Получаем цены на товары
print(f"Цена яблок в магазине '{store1.name}': {store1.get_price('яблоки')}")
print(f"Цена моркови в магазине '{store2.name}': {store2.get_price('морковь')}")
print(f"Цена молоко в магазине '{store3.name}': {store3.get_price('молоко')}")  # Товар отсутствует

# Выводим информацию о магазинах
print(store1)
print(store2)
print(store3)