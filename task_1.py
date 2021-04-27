"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.


2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""
from collections import Counter


def build_tree(string):  # Функция возвращает дерево Хаффмана
    counter = Counter(string)  # Считаем как часто встречаются символы
    if len(counter) == 1:
        return string[0]
    while len(counter) != 1:
        a, b = counter.most_common()[-2:]  # Выбираем два элемента, которые имеют минимальную частоту
        huffman_tree = Tree(a[1] + b[1], a[0], b[0])  # Создаем дерево
        del counter[a[0]]
        del counter[b[0]]
        counter[
            huffman_tree] = huffman_tree.root
    return list(counter.keys())[0]


class Tree:  # Простой класс дерева
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right


def read_tree(huffman_tree, dictionary = None, s = ''):
    if dictionary is None:
        dictionary = dict()
    if isinstance(huffman_tree, str):
        dictionary[huffman_tree] = s
        return {huffman_tree: '1'}
    read_tree(huffman_tree.left, dictionary, s + '0')
    read_tree(huffman_tree.right, dictionary, s + '1')
    return dictionary


def decode(string, dictionary):  # Функция, которая принимает закодированную строку
    reversed_dictionary = {value: key for key, value in dictionary.items()}
    res = s = ''
    for sym in string:
        s += sym
        decoded = reversed_dictionary.get(s)
        if decoded is not None:
            res += decoded
            s = ''
    return res


source_string = input ('Введите строку для кодирования: ')

tree = build_tree(source_string)
codes = read_tree(tree)

new_string = ''
for el in source_string:
    new_string += codes[el]

print('Исходная строка:', source_string)
print('Словарь кодов Хаффмана:', codes)
print('Закодированная строка:', new_string)
print('Декодированная строка:', decode(new_string, codes))

"""
Введите строку для кодирования: Вова любит 2 ложки сахара
Исходная строка: Вова любит 2 ложки сахара
Словарь кодов Хаффмана: {'х': '00000', 'р': '00001', 'к': '00010', 'с': '00011', 'л': '0010', 'и': '0011', ' ': '010', '2': '01100', 'ж': '01101', 'б': '01110', 'т': '01111', 'в': '10000', 'ю': '10001', 'В': '1001', 'о': '101', 'а': '11'}
Закодированная строка: 100110110000110100010100010111000110111101001100010001010101101000100011010000111100000110000111
Декодированная строка: Вова любит 2 ло
"""