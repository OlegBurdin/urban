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
    users = []  # список объектов User
    videos = []  # список объектов Video
    current_user = None  # текущий пользователь, User
    def log_in(self, login, password):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname in user.nickname:
                print(f"Пользователь {nickname} уже существует")
                break
        else:
             user = User(nickname, password, age)
             self.users.append(user)
             self.current_user = user
             self.log_out()
             self.log_in(user.nickname, user.password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not video == video.title:
                self.videos.append(video)

    def get_videos(self, word):
        list_video = []
        for video in self.videos:
            if word.upper() in video.title.upper():
                list_video.append(video.title)
        return list_video

    def watch_video(self, word):
        if self.current_user and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста, покиньте страницу')
        elif self.current_user:
            for video in self.videos:
                if word in video.title:
                    for second in range(video.time_now + 1, video.duration + 1):
                        print(second, end=' ')
                        sleep(1)
                    print("Конец видео")
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

    def __str__(self):
        return f"{self.videos}"

if __name__ == '__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    # Добавление видео
    ur.add(v1, v2)
    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
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
    =>
    D:\proj\pythonProject4\.venv\Scripts\python.exe D:\proj\pythonProject4\module_5_hard.py 
['Лучший язык программирования 2024 года']
['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
Войдите в аккаунт, чтобы смотреть видео
Вам нет 18 лет, пожалуйста, покиньте страницу
1 2 3 4 5 6 7 8 9 10 Конец видео
Пользователь vasya_pupkin уже существует
urban_pythonist

Process finished with exit code 0
