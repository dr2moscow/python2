"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
import timeit
from collections import OrderedDict


def remove_for_dict(dictionary):
    dictionary[0] = 0
    del dictionary[0]


d = dict()
od = OrderedDict()

print(timeit.timeit('d[0] = 0', setup='from __main__ import d', number=10**7))
print(timeit.timeit('od[0] = 0', setup='from __main__ import od', number=10**7))

print(timeit.timeit('d[0]', setup='from __main__ import d', number=10**7))
print(timeit.timeit('od[0]', setup='from __main__ import od', number=10**7))

print(timeit.timeit('remove_for_dict(d)', setup='from __main__ import d, remove_for_dict'))
print(timeit.timeit('remove_for_dict(od)', setup='from __main__ import od, remove_for_dict'))

"""
0.4016633
0.6464275
0.39335469999999995
0.30480549999999984
0.12863480000000016
0.1987561
"""

# В среднем, OrderedDict чуть медленнее обычного словаря.
# Если Python от 3.6, то можно обойтись без OrderedDict
