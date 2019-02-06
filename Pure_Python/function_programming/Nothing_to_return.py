"""
В конец любой функции Python добавляет неявную инструкцию return
None. По этой причине, если в функции не указано возвращаемое значение,
по умолчанию она возвращает None.
"""
def foo1(value):
    if value:
        return value
    else:
        return None

def foo2(value):
    """Пустая инструкция return подразумевает `return None`"""
    if value:
        return value
    else:
        return

def foo3(value):
    """Пропущенная инструкция return подразумевает `return None`"""
    if value:
        return value
