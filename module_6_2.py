
class Vehicle:
    __COLOR_VARIANTS = ['Red', 'Green', 'Blue', 'White', 'Black', 'Yellow', 'Gray']      # Доступные цвета
    def __init__(self,owner, __model, __engine_power, __color):
        self.owner =str(owner)                     # владелец транспорта. (владелец может меняться)
        self.__model = str(__model)                # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = int(__engine_power)  # мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__color = str(__color)                # название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self,):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        old_color = [color.lower() for color in self.__COLOR_VARIANTS]
        if new_color.lower() in old_color:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['Red', 'Green', 'Blue', 'White', 'Black', 'Yellow', 'Gray']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

## Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
#
## Проверяем что поменялось
vehicle1.print_info()

#Модель: Toyota Mark II
#Мощность двигателя: 500
#Цвет: blue
#Владелец: Fedos
#Нельзя сменить цвет на Pink
#Модель: Toyota Mark II
#Мощность двигателя: 500
#Цвет: BLACK
#Владелец: Vasyok