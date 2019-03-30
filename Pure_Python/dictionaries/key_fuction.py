import operator
xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
sorted(xs.items(), key=lambda x: x[1])

"""
На самом деле этот принцип настолько распространен, что стандартная
библиотека Python включает модуль operator . Этот модуль реализует
часть наиболее часто используемых функций ключа в качестве структур-
ных блоков, автоматически конфигурируемых по принципу plug-and-play,
таких как operator.itemgetter и operator.attrgetter .
Ниже приведен пример того, как можно заменить поиск по индексу на
основе лямбды в первом примере на operator.itemgetter :
"""
sorted(xs.items(), key=operator.itemgetter(1))
