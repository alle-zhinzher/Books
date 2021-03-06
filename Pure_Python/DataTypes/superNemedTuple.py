from typing import NamedTuple


class Car(NamedTuple):
    цвет: str
    пробег: float
    автомат: bool


car1 = Car('красный', 3812.4, True)
# Экземпляры имеют хороший метод repr:
print(car1)
# Доступ к полям:
print(car1.пробег)
# Поля неизменяемы:
# Аннотации типа не поддерживаются без отдельного
# инструмента проверки типов, такого как mypy:
print(Car('красный', 'НЕВЕЩЕСТВЕННЫЙ', 99))
