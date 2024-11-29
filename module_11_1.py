import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageGrab, ImageEnhance
import time




print('Библиотека Python: nympy')
class NumPy:
    arr = np.arange(1, 20, 2)              # Создание массива с диапазоном от 1 до 20 c шагом 2
    sum_ = arr.sum()                       # Суммируем массив
    resh_ = arr.reshape(2, 5)              # Преобразуем массив в другой вид  (матрица)

    print(arr)
    print(sum_)
    print(resh_)


print('Библиотека Python: matplotlib')
class MPL:

    year = [1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998,
            1999, 2000]
    people = [112266, 120766, 127189, 130704, 134690, 139028, 143835, 148543, 148704, 148673, 148366, 148306,
                  147976, 147502, 147105, 146693, 145925, 144808]


    plt.plot(year, people)              # Построение линейного графика

    plt.xlabel('Год')
    plt.ylabel('Численность [млн.ч]')
    plt.title('Населения России')
    plt.show()

print('Библиотека Python: pillow')
class PL:

    time.sleep(2)                                                     # делаем задержку в 2 секунды на выбор
                                                                      # окна, для которого нужно сделать скриншот

    img_tmp = ImageGrab.grab()                                        # создание скриншота

    img_tmp.save('test-Brightness.jpg')                               # сохраним оригинал

    for factor in [0, 0.5, 2]:

        # меняем Яркость
        img = ImageEnhance.Brightness(img_tmp).enhance(factor)       # меняем Яркость

        img.save(f'test-Brightness-{factor}.jpg')                    # сохраним измененное изображение