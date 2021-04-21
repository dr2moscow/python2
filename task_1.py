"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
import numpy as np
from memory_profiler import profile



# Python 3.9.0 x64
@profile()
def function_1(n):
    res = list(range(n))
    return res


@profile()
def function_2(n):
    res = np.arange(0, n)
    return res


function_1(10 ** 5)
function_2(10 ** 5)

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    65     30.5 MiB     30.5 MiB           1   @profile()
    66                                         def function_1(n):
    67     34.3 MiB      3.8 MiB           1       res = list(range(n))
    68     34.3 MiB      0.0 MiB           1       return res

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    71     31.3 MiB     31.3 MiB           1   @profile()
    72                                         def function_2(n):
    73     31.3 MiB      0.0 MiB           1       res = np.arange(0, n)
    74     31.3 MiB      0.0 MiB           1       return res
"""


# Использование numpy массивов уменьшает объем используемой памяти
# Задача: получить целые числа от 0 до N.
# Функция, использующая numpy, использует приблизительно в 10 раз меньше памяти, чем функция, возвращающяя список.

@profile
def find_pair1(arr):
    result = None
    for pair in arr:
        i = sum(pair)
        if result is None or i > result:
            result = i
    return result


@profile
def find_pair2(arr):
    pair_sums = [sum(pair) for pair in arr]
    return max(pair_sums)


set = np.random.randint(0, 10 ** 4, (10 ** 5, 2), dtype = np.int16)
find_pair1(set)
find_pair2(set)

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     30.8 MiB     30.8 MiB           1   @profile
    29                                         def find_pair1(arr):
    30     30.8 MiB      0.0 MiB           1       res = None
    31     30.8 MiB      0.0 MiB      100001       for pair in arr:
    32     30.8 MiB      0.0 MiB      100000           s = sum(pair)
    33     30.8 MiB      0.0 MiB      100000           if res is None or s > res:
    34     30.8 MiB      0.0 MiB          13               res = s
    35     30.8 MiB      0.0 MiB           1       return res


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    38     30.8 MiB     30.8 MiB           1   @profile
    39                                         def find_pair2(arr):
    40     35.2 MiB      4.4 MiB      100003       pair_sums = [sum(pair) for pair in arr]
    41     35.2 MiB      0.0 MiB           1       return max(pair_sums)
"""

# Количество используемой памяти зависит от способа решения задачи.
# Например, имеется двумерный массив размером n x 2
# Надо найти максимальную сумму двух чисел, которые являются парой.
# Можем искать сумму каждой пары и проверять не больше ли она максимальной (классический способ)
# А можем создать список сумм и найти в нем максимальное значение - это проще, но памяти тратиться больше!
