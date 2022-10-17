# 23.2 Обработка исключений: операторы try except

import random
import os

try:

    # Этот блок запрашивает имя файла и записывает в него случайные 10 значений возраста
    # user_file = input('Введите имя файла куда будут записаны значения возраста: ')
    # ages_file = open(f'{user_file}.txt', 'x', encoding='utf-8')
    # [ages_file.write(str(random.randint(10, 99)) + '\n') for age in range(10)]
    # ages_file.close()

    user_file = input('Введите имя файла: ')
    user_path = os.path.abspath(user_file)
    print(user_path)
    ages_file = open(''.join([user_path, '.txt' if not user_file.endswith('.txt') else '']), 'r', encoding='utf-8')
    ages_db = ages_file.read()
    ages_file.close()

    names_file = open('names_db.txt', 'r', encoding='utf-8')
    names_db = names_file.read()
    names_file.close()

    ages_db = ages_db.split()
    names_db = names_db.strip().split(', ')

    try:
        result_file = open('result.txt', 'x', encoding='utf-8')
    except FileExistsError:
        print('Ой. Файл уже существует')
        user_answer = ''
        while user_answer != 'y' and user_answer != 'n':
            user_answer = input('Хотите переписать файл?').lower()
        if user_answer == 'y':
            result_file = open('result.txt', 'w', encoding='utf-8')

            for age in ages_db:
                try:
                    result_file.write(f'{str(int(age))} - {random.choice(names_db)}\n')
                except ValueError as exc:
                    print(f'Нашлась ошибка в файле {user_file if user_file.endswith(".txt") else f"{user_file}.txt"}')
                    print(f'Исключение: {exc}')
                    print(f'Тип исключения: {type(exc)}')
            result_file.close()
        else:
            print('Никаких изменений не было внесено.')


except FileNotFoundError as exc:
    print('Такого файла не существует')
    print(f'Исключение: {exc}')
    print(f'Тип исключения: {type(exc)}')


