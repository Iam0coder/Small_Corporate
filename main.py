class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access = 'user'  # Уровень доступа по умолчанию для обычных пользователей

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access(self):
        return self.__access

    def set_name(self, name):
        self.__name = name

    def info(self):
        access_description = "Обычный уровень" if self.__access == 'user' else "Доступ отсутствует"
        print(f"ID пользователя {self.__name}: {self.__user_id}")
        print(f"Уровень доступа пользователя {self.__name}: {access_description}")


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access = 'admin'  # Повышенный уровень доступа для администраторов
        self.__user_db = []  # База данных пользователей

    def add_user(self, user_id, name):
        new_user = User(user_id, name)
        self.__user_db.append(new_user)
        print(f"Пользователь {name} добавлен в базу данных с ID: {user_id}")

    def remove_user(self, user_id):
        for i, user in enumerate(self.__user_db):
            if user.get_user_id() == user_id:
                removed_user = self.__user_db.pop(i)
                print(f"Пользователь с ID: {removed_user.get_user_id()} удален из базы данных!")
                return
        print(f"Пользователь с ID: {user_id} не найден")

    def review_db(self):
        for user in self.__user_db:
            user.info()


# Добавление пользователей (не в базу данных)
user1 = User(1, "Петя")
user2 = User(2, "Вася")

# Просмотр информации о доступах пользователей
user1.info()
user2.info()

# Конфигурация роли администратора
admin = Admin(0, "Юрий")

# Добавление пользователей в базу данных с помощью прав администратора
admin.add_user(3, "Сергей")
admin.add_user(4, "Маша")

# Просмотр базы данных пользователей
admin.review_db()

# Удаление пользователя зная его ID
admin.remove_user(3)

# Просмотр измененной базы данных пользователей
admin.review_db()
