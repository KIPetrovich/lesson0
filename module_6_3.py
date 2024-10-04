class Horse:                         #класс описывающий лошадь.
                                     #Объект этого класса обладает следующими атрибутами:
    x_distance = 0                   # пройденный путь.
    sound = 'Frrr'                   # звук, который издаёт лошадь.

    def run(self, dx):               # dx - изменение дистанции, увеличивает x_distance на dx.
        self.x_distance += dx



class Eagle:                                    #класс описывающий орла.
                                                # Объект этого класса обладает следующими атрибутами:
    y_distance = 0                              # высота полёта
    _sound = 'I train, eat, sleep, and repeat'   #звук, который издаёт орёл (отсылка)

    def fly(self, dy):                         #где dy - изменение дистанции, увеличивает y_distance на d
        self.y_distance += dy


class Pegasus(Horse, Eagle):                             #класс описывающий пегаса.
                                                         #Наследуется от Horse и Eagle в том же порядке.
    def __init__(self):
        self.x_distance = super().x_distance
        self.sound = super().sound
        self.y_distance = super().y_distance
        self.sound = super()._sound

    def move(self, dx, dy):             # где dx и dy изменения дистанции.
        self.run(dx)                    # В этом методе должны запускаться наследованные методы run и fly соответственно.
        self.fly(dy)                    # run и fly соответственно.

    def get_pos(self):                                             # возвращает текущее положение пегаса в виде кортежа -
        pos_Pegasus = (self.x_distance, self.y_distance)                    # (x_distance, y_distance) в том же порядке.
        return pos_Pegasus

    def voice(self):
        print(self.sound)               #который печатает значение унаследованного атрибута sound.


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()

