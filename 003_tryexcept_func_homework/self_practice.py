import random
# 1 Функция которая выбрасивает случаено одно из исключений
import random

error_list = [
    (TypeError, 'Error1'),
    (ValueError, 'Error2'),
    (RuntimeError, 'Error3')
]

# random.shuffle(error_list)
error, message = random.choice(error_list)
print(error, message)


def random_error_maker():
    try:
        raise error
    except ValueError:
        print('Value Error Here!')
    except TypeError:
        print('Type Error Here!')
    except RuntimeError:
        print('RunTimeError Here!')


random_error_maker()
print(str('---------------------------------------------/'))

# 2 Которая принимает список на входб и если все элементы списка числа отсортировать их
list1 = [9, 43, 2, 87, 13, 43, 24, 12, 1, 5]
list2 = ['as', 23, False, None, 3.23, 'ds']


def check_sort_list(in_list):
    try:
        for item in in_list:
            if not isinstance(item, int):
                raise ValueError
    except ValueError as e:
        print('ValueError: value is not integer!', e)
    else:
        in_list.sort()


print('list before func: ', list1)
check_sort_list(list1)
print('list after func: ', list1)
check_sort_list(list2)
print(str('---------------------------------------------/'))

# 3 Функция которая принимает словарьб преобразует все ключи словаря вк сторкам и возвращает словарь
my_dict = {1: 'aaa', 2: 'bbbb', 3: 'ccccc', 4: 'ddddd', 5: 'eeeee'}


def key_change_dict(dict):
    new_dict = {}
    for key, value in dict:
        new_dict[key[value]] = str(dict[key])
    return new_dict


print('before func: ', my_dict)
dict2 = key_change_dict(my_dict)
print(dict2)
print(str('---------------------------------------------/'))


# 4 Принимает список чисел и возвращает их произвдение.
list_num = [1, 3, 4, 5]


def multiply_list(numbers):
    mul = 1
    for item in numbers:
        mul *= item
    return mul


print(list_num, 'multiply...')
print(multiply_list(list_num))
