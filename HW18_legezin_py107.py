num1 = int(input('Введите первое число:'))
num2 = int(input('Введите второе число:'))
while num2 == 0:
    num2 = int(input('Введите второе число:'))
try:
    print(num1 / num2)
except ZeroDivisionError:
    print('Ошибка деления на ноль:')
except TypeError:
    print('Введен неверный тип данных:')