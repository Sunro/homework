# Классы и объекты
class Human:
    pass
class Human2:
    def __init__(self):
        self.name = 'Дэн'
class Human3:
    def __init__(self, name):
        self.name = name
den = Human()
max = Human()
alex = Human2()
jack = Human3('Джек')

print(type(5))
print(id(den), id(max))
print(den)
print(max)
print(alex.name)
print(jack.name)

# Атрибуты и методы объекта. Указатель на свой объект в методах
# __init__(self, ) - конструктор, инициализатор
class Human4:

    head = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'Я {self.name} и у меня день рождения, мне теперь {self.age}')

    def __str__(self):
        return f'{self.name}'

    def __len__(self):
        return self.age

    def __lt__(self, other):
        return self.age < other.age

    def __qt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.age == other.age and self.age == other.age

    def __bool__(self):
        return bool(self.age)

    def __del__(self):
        print(f'{self.name} ушёл')

joy = Human4('Джой', 33)
ros = Human4('Рос', 32)
print(joy.name, joy.age)
joy.surname = 'Трибиани'
print(ros.name, ros.age)
print(joy.surname)
joy.say_info()
ros.say_info()
joy.birthday()

# Специальные методы классов
# методы содержащие __ подчеркивание
# называются специальными или магическими
# Также можно встретить другое название — dunder-методы,
# что является сокращением от фразы "double underscore

del ros
joy.birthday()
# input()
print(len(joy))

# Перегрузка операторов
max.name = 'Денис'
den = Human4('Дэн', 33)
max = Human4('Макс', 32)
print(den == max, f'сравнение возраста {den.name} и {max.name}')
max.birthday()
print(max == den, f'сравнение возраста {den.name} и {max.name}')
# print('сравнение возраста Макса и Дена 2')
print(den)
print(max)

# Различие атрибутов класса и экземпляра. Пространство имен класса
print(Human4.head)
print(Human4.__dict__)
print(den.__dict__)
Human4.head = 2
print(Human4.__dict__)
den.head = 3
print(den.__dict__)

# ПКМ run in python console
# Human4.head = False



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 5.6 Класс object и метод __new__
print(int.__mro__)
print(object)

class User:
    def __new__(cls, *args, **kwargs):
        print('Я в нью')
        # if cls.__instance is None:

    # зачем нужо переопределять класс, к примеру singleton. когда нужно
    # чтоб экземпляр класса создавался единожды
    def __init__(self):
        print('Я в ините')

user1 = User()
print(User.__mro__)
print(user1)

# self - указатель на объект/экземпляр класса
# cls - указатель на калсс

class User2:
    # __instance = None
    def __new__(cls, *args, **kwargs):
        print('Я в нью2')
        # if cls.__instance is None:
        return super().__new__(cls)
        # if cls.__instance is None:

    # зачем нужно переопределять класс, к примеру singleton. когда нужно
    # чтоб экземпляр класса создавался единожды
    def __init__(self):
        print('Я в ините2')

user1 = User2()
user2 = User2()
print(User2.__mro__, 'User2.__mro__')
print(user1 is user2, 'user1 is user2')
print(id(user1), id(user2), 'id(user1), id(user2)')

# user1 = User2()
print(user1, 'user1')

class User3:
    __instance = None
    def __new__(cls, *args, **kwargs):
        print('Я в нью3')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return  cls.__instance

    def __init__(self):
        print('Я в ините3')

user1 = User3()
user2 = User3()
print(id(user1), id(user2))
print(user1 is user2)

class User4:
    __instance = None
    def __new__(cls, *args, **kwargs):
        print('Я в нью4')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return  cls.__instance

    def __init__(self, *args, **kwargs):
        print('Я в ините4')
        self.args = args
        self.kwargs = kwargs
        # self.name = kwargs.get('name')
        # self.age = kwargs.get('age')
        for key, values in kwargs.items():
            setattr(self, key, values)


other = [1, 2, 3]
user = {'name': 'Den', 'age': 25}
other1 = [4, 5, 6]
user1 = {'name': 'Max', 'age': 22, 'gender': 'male'}
info_user1 = User4(other, user)
info_user2 = User4(*other1, **user1)
print(info_user1.args)
print(info_user1.kwargs)
print(info_user2.args)
print(info_user2.kwargs)
print(info_user2.name)
print(info_user2.age)
print(info_user2.gender)

# user2 = User4()
# print(id(user1), id(user2))
# print(user1 is user2)



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 5_7 Практика (Система регистрации на классах). 1.1
class Database:
    def __init__(self):
        self.data = {}
    def add_user(self, username, password):
        self.data[username] = password

class User:
    """
    Класс пользователя содержащий атрибуты логин и пароль
    обратиться можно через >>> User.__doc__ в консоли
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

# if __name__ == '__main__':
#     database = Database()
#     while True:
#         choice = input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация")
#         user = User(input("Введите логин: "), password := input("Введите пароль: "), password2 := input("Повторите пароль: "))
#         if password != password2:
#             exit()
#         database.add_user(user.username, user.password)
#         print(database.data)



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Практика. 1.2
            # print(database.data)
# if __name__ == '__main__':
#     database = Database()
#     while True:
#         choice = input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация")
#         user = User(input("Введите логин: "), password := input("Введите пароль: "), password2 := input("Повторите пароль: "))
#         if password != password2:
#             exit()
#         database.add_user(user.username, user.password)
#         print(database.data)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Практика. 1.3
if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n"))
        if choice == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                print('ok')
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                    # break
                else:
                    print('Неверный пароль')
            else:
                print('Пользователь не найден: ')
        if choice == 2:
            user = User(input("Введите логин: "), password := input("Введите пароль: "), password2 := input("Повторите пароль: "))
            if password != password2:
                # exit()
                print('Пароли не совпадают, попробуйте ещё раз')
                continue
            database.add_user(user.username, user.password)
        print(database.data)