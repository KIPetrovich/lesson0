def personal_sum(numbers):                                           # Функция personal_sum(numbers)
    result = 0                                                       # начало отсчета
    incorrect_data = 0                                               # Начало отсчета
    for i in numbers:                                    # одсчитывать сумму чисел в numbers путём перебора
        try:
            result += i                                     # Увеличиваем переменную result
        except TypeError:                                            # Обрабатываем исключение по неверному типу данных
            incorrect_data += 1                                      # Увеличив счётчик incorrect_data на 1.
            print(f"Некорректный тип данных для подсчёта суммы "
                  f"- {i}")
    return result, incorrect_data                                    # Возвращает кортеж из двух значений


def calculate_average(numbers):                                                  #Функция calculate_average(numbers)
    try:
        sum_numbers, incorrect_data = personal_sum(numbers)
        if len(numbers) - incorrect_data == 0:
            raise ZeroDivisionError
        return sum_numbers / (len(numbers) - incorrect_data)                # возвращаtv: среднее арифметическое всех чисел
    except ZeroDivisionError:                                     # обработайте исключение ZeroDivisionError при пустом numbers
        return 0
    except TypeError:                                              # Обрабатываем исключение по неверному типу данных
        print("В numbers записан некорректный тип данных")
    return None


#Пример выполнения программы
print(f'Результат 1: {calculate_average("1, 2, 3")}')          # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')                  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')                                                 # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')                                    # Всё должно работать
