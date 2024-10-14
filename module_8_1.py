
def add_everything_up(a, b):

    try:
        sum_ = a + b                   # выполняем действие по сложению двух аргументов функции
        d = round(sum_, 3)             # округляем до треьего знака после плавующей точки
        return d                       # возвращаем результат сложения

    except TypeError:
        return f'{str(a)+str(b)}'         # возвращать строковое представление этих двух данных вместе


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))