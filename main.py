"""Разработай систему управления учетными записями пользователей
для небольшой компании. Компания разделяет сотрудников на обычных
работников и администраторов. У каждого сотрудника есть уникальный
идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных
данных пользователей, имеют дополнительный уровень доступа и могут добавлять
или удалять пользователя из системы.

Требования:

1. Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
ID, имя и уровень доступа ('user' для обычных сотрудников).

2. Класс Admin: Этот класс должен наследоваться от класса User.
Добавь дополнительный атрибут уровня доступа, специфичный для
администраторов ('admin'). Класс должен также содержать методы add_user и
remove_user, которые позволяют добавлять и удалять пользователей из списка
(представь, что это просто список экземпляров User).

3. Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого
доступа и модификации снаружи. Предоставь доступ к необходимым атрибутам через
методы (например, get и set методы)."""


class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access = 'user'  # Уровень доступа по умолчанию для обычных пользователей

    def get_user_id(self):
        return self.__user_id

    def get_user_name(self):
        return self.__name

    def info(self):
        access_description = "Обычный доступ" if self.__access == 'user' else "Доступ отсутствует"
        print(f"ID пользователя {self.__name}: {self.__user_id}")
        print(f"Уровень доступа пользователя {self.__name}: {access_description}")


class Admin(User):
    def __init__(self, user_id, name, access):
        super().__init__(user_id, name)
        self.__access = access
        self.__user_db = []  # База данных пользователей

    def add_user(self, user_id, name, access):
        new_user = Admin(user_id, name, access)
        self.__user_db.append(new_user)
        print(f"Пользователь {name} с доступом '{access}' добавлен в базу данных с ID: {user_id}")

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

    def info(self):
        if self.__access == 'admin':
            access_description = "Полный доступ"
        elif self.__access == 'user':
            access_description = "Обычный доступ"
        else:
            access_description = "Доступ отсутствует"
        print(f"ID пользователя {self.get_user_name()}: {self.get_user_id()}")
        print(f"Уровень доступа пользователя {self.get_user_name()}: {access_description}")


# Добавление администратора (не в базу данных)
admin = Admin(0, "Юрий", "admin")

# Добавление пользователей (не в базу данных)
user1 = User(1, "Петя")
user2 = User(2, "Вася")

print("\n==========================================================================")
print("============== Просмотр информации о доступах пользователях ==============\n")
admin.info()
user1.info()
user2.info()

print("\n==========================================================================")
print("== Добавление пользователей в базу данных с помощью прав администратора ==\n")
admin.add_user(3, "Сергей", "user")
admin.add_user(4, "Маша", "admin")

print("\n==========================================================================")
print("=================== Просмотр базы данных пользователей ===================\n")
admin.review_db()

print("\n==========================================================================")
print("=================== Удаление пользователя зная его ID ====================\n")
admin.remove_user(3)

print("\n==========================================================================")
print("============== Просмотр измененной базы данных пользователей =============\n")
admin.review_db()
