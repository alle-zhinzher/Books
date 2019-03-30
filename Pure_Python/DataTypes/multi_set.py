'''
Класс collections.Counter стандартной библиотеки Python реализует
тип «мультимножество» (или «мешок»), который допускает неоднократ-
ное появление элемента в множестве

Общие структуры данных Python
Это бывает полезно, если вам нужно вести учет не только того, при-
надлежит ли элемент множеству, но и того, сколько раз он был включен
в множество:
'''
from collections import Counter
inventory = Counter()
loot = {'клинок': 1, 'хлеб': 3}
inventory.update(loot)
print(inventory)
more_loot = {'клинок': 1, 'яблоко': 1}
inventory.update(more_loot)
print(inventory)

len(inventory)
# Количество уникальных элементов
sum(inventory.values())
# sОбщее количество элементов
