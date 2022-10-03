# 23.2 Обработка исключений: операторы try except

import random

try:

    ages_file = open('ages.txt', 'x', encoding='utf-8')
    [ages_file.write(str(random.randint(10, 99)) + '\n') for age in range(10)]
    ages_file.close()

    ages_file = open('ages.txt', 'r', encoding='utf-8')
    ages_db = ages_file.read()
    ages_file.close()

    names_file = open('names_db.txt', 'r', encoding='utf-8')
    names_db = names_file.read()
    names_file.close()

    ages_db = ages_db.split()
    names_db = names_db.strip().split(', ')

    result_file = open('result.txt', 'w', encoding='utf-8')
    for age in ages_db:
        result_file.write(f'{str(age)} - {random.choice(names_db)}\n')
    result_file.close()

except FileExistsError as exc:
    print(f'Файл ages.txt уже существует.')
    print(f'Исключение: {exc}')
    print(f'Тип исключения: {type(exc)}')




