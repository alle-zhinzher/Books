"""
Как могла бы выглядеть реализация простого декоратора? В общих чертах
декоратор — это вызываемый объект, который на входе принимает один
вызываемый объект, а на выходе возвращает другой вызываемый объект.
Приведенная ниже функция имеет это свойство и может считаться самым
простым декоратором, который вы могли когда-либо написать:
"""

def null_decorator(func):
    return func


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def greet():
    return 'Привет!'

"""
Возможно, вас не удивит, что к функции можно применять более одного
декоратора. В этом случае их эффекты накапливаются, и именно этот
факт делает декораторы столь полезными в качестве структурных блоков
многократного использования
"""

def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper


@strong
@emphasis
def greet():
    return 'Привет!'