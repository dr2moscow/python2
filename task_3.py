"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


@profile
def call(function, *args, **kwargs):
    return function(*args, **kwargs)


call(factorial, 700)

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     19.0 MiB     19.0 MiB           1   @profile
    30                                         def call(function, *args, **kwargs):
    31     20.2 MiB      1.3 MiB           1       return function(*args, **kwargs)
"""

# Рекурсивная функция вызывается не один раз, результат профилирования с помощью декоратора будем получать разный
# при каждом вызове функции, это не даст представления об использовании памяти.
# Добавляем новую функцию, которая будет применять декоратор для вызова рекурсивную функцию.
