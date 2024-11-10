import threading
import  time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)

    def run(self):
        print(f'{self.name}, на нас напали!')
        num_days = 0
        enemyes = 100
        while enemyes > 0:
            time.sleep(1)
            num_days += 1
            enemyes = enemyes - self.power

            if enemyes < 0:
                enemyes = 0
            print(f'{self.name} сражается {num_days}..., осталось {enemyes} воинов.')
        print(f'{self.name} одержал победу спустя {num_days} дней(дня)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print('Все битвы закончились!')

