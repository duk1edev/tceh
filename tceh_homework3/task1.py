# 1
number = int(input("Enter the number: "))

try:
    if number % 2 == 0:
        raise ValueError
    if number < 0:
        raise TypeError
    if number > 10:
        raise IndexError
except ValueError:
    print("You raise a Value Error")
except TypeError:
    print("You raise a TypeError")
except IndexError:
    print("You raise a IndexError")

# 2
my_list = [12, 321, 3, 157, 'jeka', 'ibragim', 'mo4alka']

try:
    index = int(input('Enter the element index: '))
    print(my_list[index])
except IndexError as e:
    print("Entered index is out of range", e)
except ValueError as e:
    print("Index must be integer!!!", e)


# Functions
# --------------------------------------------
# 1
def sum_or_sub(a, b):
    if a > 0 and b > 0:
        return a + b
    if a < 0 and b < 0:
        return a - b
    else:
        return 0


print(sum_or_sub(1, 1))


# 2
def double_max(a, b, c):
    lst = [a, b, c]

    max1 = max(lst)
    print('Max1 = ', max1)
    lst.remove(max1)
    max2 = max(lst)
    print('Max2 = ', max2)


double_max(23, 32, 12)


# 3
def returns_numbers(args: list, flag: bool):
    new_lst = []
    if flag:
        for num in args:
            if num % 2 != 0:
                new_lst.append(num)
    if not flag:
        for num in args:
            if num % 2 == 0:
                new_lst.append(num)

    return new_lst


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(returns_numbers(list1, True))
print(returns_numbers(list1, False))


# **Задачи на закрепление типов аргументов:
# 1
def max_min(args: int):
    return max(args), min(args)


list2 = [132, 22, 313, 324, 2315, 316, 327, 8313123]
print(max_min(list2))


# 2
def return_strings(my_str: str, flag=True):
    new_str = ''
    if flag:
        new_str = my_str.lower()
    if not flag:
        new_str = my_str.upper()
    return  new_str


print(return_strings('asddAAAAAAAAAAAsfDsadsfsdgsdg'))
print(return_strings('asSDdasfSDASDsfssDgDsdD', False))

# 3
def noname_func(*args: str, glue=":"):
    str_list = []
    for item in args:
        if len(item) > 3:
            print(item, glue)

    return 0
