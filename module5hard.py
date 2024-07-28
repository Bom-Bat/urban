from time import sleep as sleep__


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.adult_mode = adult_mode
        self.duration = duration
        self.title = title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        self.age = 0

    def register(self, nickname, password, age):
        if self.users.__eq__([]):
            self.users.extend([nickname, hash(password), age])
            self.current_user = nickname
            self.age = age
            return self
        else:
            for i in range(0, len(self.users), 3):
                if nickname != self.users[i]:
                    self.users.extend([nickname, hash(password), age])
                    self.current_user = nickname
                    self.age = age
                else:
                    print(f'Пользователь {nickname} уже существует\033[34m')
                    break
            return self

    def log_in(self, nickname, password):
        for i in range(0, len(self.users), 3):
            if nickname.__eq__(self.users[i]):
                if hash(password) == self.users[i+1]:
                    self.current_user = nickname
                else:
                    print(f'\033[31mВведен не верный пароль!')
                    ur.log_out(self.current_user)
            else:
                print(f'\033[32mЗдравствуйте {self.current_user}')

    def log_out(self, current_user):
        print(f'\033[32mПользователь {current_user} покинул  UrTube')
        self.current_user = None
        return self

    def add(self, *args):
        for i in args:
            if i.title not in self.videos:
                self.videos.extend([i.title, i.duration, i.adult_mode])
            print(f'\033[34m{self.videos[::3]}')
        return self

    def get_videos(self, var):
        for i in range(0, len(self.videos), 3):
            if var.lower() in self.videos[i].lower():
                return self.videos[i]
        return f'\033[31mНи чего не найдено'

    def watch_video(self, title):
        for i in range(0, len(self.videos), 3):
            if title.__eq__(self.videos[i]):
                if self.current_user is None:
                    return print(f'\033[32mВойдите в аккаунт, чтобы смотреть видео')
                else:
                    if self.videos[i + 2] and self.age.__lt__(18):
                        print(f'\033[31mВам нет 18 лет, пожалуйста покиньте страницу')
                        ur.log_out(self.current_user)
                    else:
                        duration = self.videos[i+1]
                        for j in range(duration):
                            print(f'\033[33m{j + 1} * ', end='')
                            sleep__(1)
                        print('Конец видио')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 20)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('чего'))
    # print(ur.get_videos('пень'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
