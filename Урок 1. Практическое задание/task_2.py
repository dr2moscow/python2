"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""


# 1. Функция поиска минимального значания из списка, сложность O(n^2) - квадратичная
def min_search(min_list):
    min_o = min_list[0]
    for el in min_list:
        for el2 in min_list:
            if el < el2 and el < min_o:
                min_o = el
    return min_o


# 2. Функция поиска минимального значания из списка, сложность O(n) - линейная
def min_search_2(min_list):
    min_o = min_list[0]
    for el in min_list:
        if el < min_o:
            min_o = el
    return min_o


l = [2, 7, 9, 12, 33, 5, 0, -2, -5]

print(min_search(l))
print(min_search_2(l))
