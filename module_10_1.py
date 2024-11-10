import time
from time import sleep
import threading
def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='UTF-8')

    for i in range(word_count):
        file.write(f'Какое-то слово №  {i + 1}\n')
        sleep(0.1)

    file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start = time.time()

write_words (10, 'example1.txt')
write_words (30, 'example2.txt')
write_words (200, 'example3.txt')
write_words (100, 'example4.txt')

time_stop = time.time()

time_result = time_stop - time_start

print(f'Время работы функций {time_result}')


time2_start = time.time()    # Взятие текущего времени

func5 = threading.Thread(target=write_words, args= (10, 'example5.txt'))
func6 = threading.Thread(target=write_words, args= (30, 'example6.txt'))
func7 = threading.Thread(target=write_words, args= (200, 'example7.txt'))
func8 = threading.Thread(target=write_words, args= (100, 'example8.txt'))

func5.start()
func6.start()
func7.start()
func8.start()

func5.join()
func6.join()
func7.join()
func8.join()

time2_stop = time.time()
time2_result = time2_stop - time2_start
print(f'Время работы потоков {time2_result}')
