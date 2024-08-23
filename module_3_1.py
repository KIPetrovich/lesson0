
calls = 0

def count_calls():                             #Функция count_calls подсчитывающая вызовы остальных функций.
    global calls
    calls += 1


def string_info(string):                                       # Функция string_info принимает аргумент - string и возвращает кортеж из:
    result = (len(string), string.upper(), string.lower())      # длины этой строки, строку в верхнем регистре,
                                                                # строку в нижнем регистре.
    count_calls()                                               # счетчик вызовов
    return result


def is_contains(string, list_to_search):       #Создать функцию is_contains с двумя параметрами string и list_to_search
    string = string.lower()                       # переводим искомую строку в нижний регистр
    count_calls()                                        # счетчик вызовов
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:    # переводим список в нижний регистр, одновременно сравнивая его со строкой
            result = True                               #  совподение, если в списке хотябы одно слово соответствует слову в строке
            break
        else:
            result = False                                # не соответствует
            continue
    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)



#count_calls()