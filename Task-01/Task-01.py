# Задача 1. Пятый элемент

BRUCE_WILLIS = 42

input_data = input('Введите строку: ')
try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError:
    print('Невозможно преобразовать введеную строку к числу')

except IndexError:
    print('Ошибка индекса, выход за границы списка')

except:
    print('Прочие ошибки')
