
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

    def update_price(self, item_name, new_price):     # Метод для обновления цены товара.

        if item_name in self.name:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена в магазине '{self.name}'.")

        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте магазина '{self.name}'.")

    def __str__(self):     # Информация о магазине

        return f"Магазин: {self.name}, Адрес: {self.address}, Ассортимент: {self.items}"

# Создаем несколько объектов класса Store
store1 = Store("Магазин Фрукты", "ул. Ленина, 10")
store2 = Store("Супермаркет Овощи", "пр. Мира, 25")

# Добавляем товары в магазины
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)
store2.add_item("морковь", 0.3)
store2.add_item("картофель", 0.4)

# Обновляем цены на товары
store1.update_price("яблоки", 0.6)
store2.update_price("морковь", 0.35)

# Удаляем товары из ассортимента
store2.remove_item("картофель")

# Получаем цены на товары
print(f"Цена яблок в магазине '{store1.name}': {store1.get_price('яблоки')}")
print(f"Цена моркови в магазине '{store2.name}': {store2.get_price('морковь')}")
print(f"Цена картофель в магазине '{store2.name}': {store2.get_price('картофель')}")  # Товар отсутствует

# Выводим информацию о магазинах
print(store1)
print(store2)
