class UserNotFoundError(Exception):
    pass

class UserAlreadyExistError(Exception):
    pass

class User:
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age

    def __str__(self):
        return f'Имя: {self.username}, возраст: {self.age}, почта: {self.email}'

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user: User):
        if user.username in self.users:
            raise UserAlreadyExistError(f'Пользователь "{user.username}" уже существует.')
        else:
            self.users[user.username] = user

    def remove_user(self, username: str):
        try:
            del self.users[username]
        except KeyError as e:
            raise UserNotFoundError(f'Пользователя "{username}" не существует!')

    def find_user(self, username: str):
        try:
            return f'Вы искали: "{self.users[username]}".'
        except KeyError as e:
            raise UserNotFoundError(f'Пользователь с именем "{username}" не найден.')

def main():
    manager = UserManager()
    try:
        u1 = User('u', 'mail@mail.ru', 30)
        manager.add_user(u1)
        print(manager.users)

        u2 = User('k', 'mail@mail.ru', 30)
        manager.add_user(u2)
        print(manager.users)

        u3 = User('k', 'mail@mail.ru', 30)
        manager.add_user(u3)
        print(manager.users)
    except UserAlreadyExistError as u:
        print(f'Ошибка! {u}')

    try:
        manager.remove_user(u1)
        manager.add_user(u4)
        manager.remove_user(u1)
    except UserNotFoundError as e:
        print(f'Ошибка! {e}')

    try:
        print(manager.find_user('k'))
        print(manager.find_user('i'))
    except UserNotFoundError as e:
        print(f'Ошибка! {e}')

if __name__ == '__main__':
    main()


