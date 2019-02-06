"""
Это также дает вам возможность модифицировать аргументы перед тем,
как вы передадите их дальше. Вот пример:
"""
import functools


def foo(x, *args, **kwargs):
 kwargs['имя'] = 'Алиса'
 new_args = args + ('дополнительный', )
 #bar(x, *new_args, **kwargs)

"""
Данный прием может быть полезен для создания производных классов
и написания оберточных функций. Например, он может применяться
для расширения поведения родительского класса без необходимости
повторять полную сигнатуру его конструктора в дочернем классе. Это
может быть довольно удобно, если вы работаете с API, который может
измениться за пределами вашего контроля:
"""

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'синий'

print(AlwaysBlueCar('зеленый', 48392).color)

"""
написание оберточных функций, таких как декораторы.
Там вы также захотите принимать произвольные аргументы, которые будут переправляться
в обернутую функцию.
И если мы можем сделать это без необходимости копипастить сигнатуру
оригинальной функции, то, возможно, сопровождение станет удобнее:
"""

def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)
    return decorated_function

@trace
def greet(greeting, name):
    return '{}, {}!'.format(greeting, name)


print(greet('Привет', 'Боб'))
