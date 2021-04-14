"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    m = 0
    num = 0
    for i in set(array):
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(f'Функция №1: {func_1()}')
print(timeit("func_1()", "from __main__ import func_1,array"))

print(f'\nФункция №2: {func_2()}')
print(timeit("func_2()", "from __main__ import func_2,array"))

# вместо обхода всего списка, обходим только уникальные значения.
print(f'\nФункция №3: {func_3()}')
print(timeit("func_3()", "from __main__ import func_3,array"))

"""
Функция №1: Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
1.6434109000000001

Функция №2: Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
2.3602792

Функция №3: Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
1.3152967999999996
"""