def integers():
    for i in range(1, 9):
        yield i


def squared(seq):
    for i in seq:
        yield i * i


chain = squared(integers())

"""
И мы можем продолжить добавлять в этот конвейер новые структурные
блоки. Данные текут только в одном направлении, и каждый шаг обработ-
ки защищен от других четко определенным интерфейсом.
Это похоже на то, как работают конвейеры в UNIX. Мы состыковываем
последовательность процессов в цепочку так, чтобы результат каждого
процесса подавался непосредственно на вход следующего.
"""


def negated(seq):
    for i in seq:
        yield -i


chain = negated(squared(integers()))


integers = range(8)
squared = (i * i for i in integers)
negated = (-i for i in squared)