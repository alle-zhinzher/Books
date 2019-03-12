'''
Мелкая копия (shallow copy) означает конструирование нового объекта-
коллекции и затем его заполнение ссылками на дочерние объекты, най-
денные в оригинале. В сущности, мелкая копия имеет всего один уровень
в глубину. Процесс копирования выполняется нерекурсивно и поэтому не
создает копий самих дочерних объектов.

Глубокая копия (deep copy) выполняет процесс копирования рекурсивно.
Это означает конструирование сначала нового объекта коллекции, а за-
тем рекурсивное его заполнение копиями дочерних объектов, найденных
в оригинале. При копировании объекта таким способом выполняется об-
ход всего дерева объектов целиком, и создается полностью независимый
клон исходного объекта и всех его потомков.
'''

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs) # Сделать мелкую копию

import copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)
