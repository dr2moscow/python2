"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""


# Решение 1, уровень сложности O(n log n)
def top_company(comp_list):
    top = sorted(comp_list, key = comp_list.get, reverse = True)[:3]
    return top


# Решение 2, уровень сложности O(n^2)
def top_company_2(company_list, q_data):
    top = []
    max_list = []
    for i in company_list.values():
        top.append(i)
    for x in range(q_data):
        max_profit = max(top)
        max_list.append(max_profit)
        top.remove(max_profit)
    return max_list


company = {'BMW': 200100, 'AUDI': 7500, 'Sberbank': 50000, 'VTB': 222, 'Google': 921200, 'HH': 10}

print(top_company(company))
print(top_company_2(company, 3))

# Решение 1 визуально выглядит лучше и по уровню сложности лучше, т.к. сложность O(n log n) меньше, чем O(n^)
