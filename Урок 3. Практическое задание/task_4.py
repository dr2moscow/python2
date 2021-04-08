"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
from hashlib import sha256


def memorize(func):
    def get(url, memory = {}):
        write = memory.get(sha256(url.encode('utf-8')).hexdigest())
        if write is None:
            write = func(url)
            print(f'url {url} был добавлен в кеш')
            memory[sha256(url.encode('utf-8')).hexdigest()] = write
        else:
            print('не добавлен, дубликат')
        return write
    return get


@memorize
def check_url(url):
    return url


n = 1

while n == 1:
    url_input = input('Введите url (или Enter для выхода):')
    if url_input == "":
        break
    else:
        check_url(url_input)
