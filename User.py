class User:

    def __init__(self, user_id, name ):
        self._access_level = "user"
        self._user_id = user_id
        self._name = name

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

    def __str__(self):    # Метод для строкового представления пользователя

        return f"ID: {self._user_id}, Имя: {self._name}, Уровень доступа: {self._access_level}"

class Admin(User):

    def __init__(self, user_id, name):
        super().__init__(user_id, name)

        self._access_level = 'admin'   # Уровень доступа для администраторов
        self._users = []    # Список пользователей, которыми управляет администратор

    def add_user(self, user):   # Метод для добавления пользователя
        if isinstance(user, User):   # Проверяем, что добавляемый объект является пользователем
            self._users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Неверный объект пользователя.")

    def remove_user(self, user_id):   # Метод для удаления пользователя по ID
        for user in self._users:
            if user.get_user_id() == user_id:
                self._users.remove(user)
                print(f"Пользователь с ID {user_id} удален из списка.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    def show_users(self):    # Метод для отображения всех пользователей
        if not self._users:
            print("Список пользователей пуст.")
        else:
            print("Список пользователей:")
            for user in self._users:
                print(user)

# Пример использования

# Создаем обычных пользователей
user1 = User(1, "Иван Иванов")
user2 = User(2, "Мария Петрова")

# Создаем администратора
admin = Admin(100, "Игорь Петрович")

# Администратор добавляет пользователей
admin.add_user(user1)
admin.add_user(user2)

# Выводим список пользователей
admin.show_users()

# Администратор удаляет пользователя
admin.remove_user(1)

# Снова выводим список пользователей
admin.show_users()

# Пытаемся добавить неверный объект (не User)
admin.add_user("Не пользователь")