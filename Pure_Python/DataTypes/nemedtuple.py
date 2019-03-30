from collections import namedtuple
Car = namedtuple('Авто', 'цвет пробег автомат')
car1 = Car('красный', 3812.4, True)
# Экземпляры имеют хороший метод repr:
print(car1)
# Доступ к полям:
print(car1.пробег)

# Поля неизменяемы:
