import sys


# Recursion

# Run this in pythontutor.com


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(4))

sys.getrecursionlimit()
#print(factorial(4000))


# More realistic example

def double_all_elements(lst):
    """
    Double all elements in list
    :param lst: incoming list
    :return: result list
    """

    if len(lst) == 0:
        return []
    else:
        update_elements = lst[0] * 2
        print(update_elements, len(lst))
        result = [update_elements, ] + double_all_elements(lst[1:])
    return result


# Convert to tail recursion

def double_all_elements(lst, result_lst=None):
    """
    Double all elements in list (tail recursions example)

    :param lst: incoming list
    :param result_lst:
    :return: result list
    """

    if result_lst is None:
        result_lst = []

    if len(lst) == 0:
        return result_lst
    else:
        updated_element = lst[0] * 2
        result_lst.append(updated_element)
        print(updated_element, len(lst), result_lst)
        result = double_all_elements(lst[1:], result_lst)
        print(result)
    return result


# Convert recursion to loop
def double_all_elements(lst, result_lst=None):
    """
    Double all elements without recursion
    :param lst: incoming list
    :param result_lst:
    :return: result list
    """
    if result_lst is None:
        result_lst = []

    while len(lst) > 0:
        updated_element = lst[0] * 2
        print(updated_element, len(lst), result_lst)
        (lst, result_lst) = (lst[1:], result_lst + [updated_element, ])
    return result_lst


def print_all_list_items(data):
    if not data:
        return
    item = data.pop()
    print(item)
    return print_all_list_items(data)


new_list = print_all_list_items(['1', '3', 'end'])
print(new_list)
