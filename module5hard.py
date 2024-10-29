from time import sleep
class User:
    def __init__(self, nickname, password, age):  # инициализация данных:
        self.nickname = nickname  # имя пользователя (строка)
        self.password = password  # пароль (число)
        self.age = age  # возраст (число)

    def __hash__(self):
        return hash(self.password)

    def __str__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        return self.nickname == other.nickname


class Video:
    title = None

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title  # заголовок, строка
        self.duration = duration  # продолжительность, секунды
        self.time_now = time_now  # секунда остановки (изначально 0)
        self.adult_mode = adult_mode  # ограничение по возрасту, bool (False по умолчанию)

    def __str__(self):
        return f'{self.title}'


class UrTube:

    def __init__(self):  #
        self.users = []  # список объектов User
        self.videos = []  # список объектов Video
        self.current_user = None  # текущий пользователь, User

    def log_in(self, nickname, password):
        for user in self.users:
            if self.nickname == nickname and self.password == hash(self, password):
                self.current_user = user
        print('Пользователя нет в списке')

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == self.nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            self.videos.append(video)

    def get_videos(self, text):
        list_movie = []
        for text in self.videos:
            if text.upper() in Video.title.upper():
                list_movie.append(Video.title)
        return list_movie

    def watch_video(self):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for name_of_film in Video.title:
            if name_of_film == Video.title:
                if self.current_user and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for second in range(Video.time_now, Video.duration):
                    print(f"Секунда: {second + 1}")
                    sleep(1)
                    Video.time_now = 0
                    print("Конец видео")

    def __str__(self):
        return f"{self.videos}"

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
