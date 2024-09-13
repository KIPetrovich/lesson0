


def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()                                             # ничего не возвращает

inner_function()                                                 # Выдает ошибку т.к. в не поле видимости


test_function()                                                  #  Выводит "Я в области видимости функции test_function"