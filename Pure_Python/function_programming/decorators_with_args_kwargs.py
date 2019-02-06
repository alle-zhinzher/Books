def trace(func):
    def wrapper(*args, **kwargs):
        print('+++')
        print(f'ТРАССИРОВКА: вызвана {func.__name__}() с {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'ТРАССИРОВКА: {func.__name__}() вернула {original_result!r}')
        return original_result
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


say("Jey", 'Hello')


"""Декоратор functools.wraps можно использовать в своих собственных
декораторах для того, чтобы копировать потерянные метаданные из
 недекорированной функции в замыкание декоратора. Вот пример:
"""
import functools
def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper