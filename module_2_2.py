from time import sleep

text = ('Введите три числа:')
print(text)
sleep(3)
first = input('Введите первое число  ')
second = input('Введите второе число  ')
third = input('Введите третье число  ')

if first == second == third:
    print(3)
elif(first == second or
     first == third or
     second == third):
    print(2)
else:
    print(0)