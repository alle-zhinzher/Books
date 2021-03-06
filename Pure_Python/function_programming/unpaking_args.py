def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))

"""
Размещение звездочки * перед итерируемым объектом в вызове функции
его распакует и передаст его элементы как отдельные позиционные 
аргументы в вызванную функцию.
"""

tuple_vec = [0, 5, 2]
print_vector(*tuple_vec)

"""
** для распаковки именованных аргументов, поступающих
из словарей
"""
dict_vec = {'y': 0, 'z': 1, 'x': 1}
"""
Поскольку словари не упорядочены, этот оператор соотносит значения
словаря и аргументы функции на основе ключей словаря: аргумент x
получает значение, связанное в словаре с 'x'.
"""
print_vector(**dict_vec) 