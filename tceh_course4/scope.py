def scoped_function(arg):
    value = arg * 10
    print(value)


scoped_function(25)

def return_some(input_value):
    calc = input_value - 7
    print(calc)
    return calc


print(return_some(4))

# GLOBAL SCOPE

SOME_VAR = 'value'


def print_var():
    print(SOME_VAR)


print_var()

# You can not modify


def modify_var():
    try:
        SOME_VAR += 'extra'
    except UnboundLocalError as e:
        print('Error: ', e)


modify_var()
print(SOME_VAR)


# But you can mutate it

GLOBAL_LIST = []


def append_to_list(item):
    print('Adding', item)
    GLOBAL_LIST.append(item)


append_to_list(1)
append_to_list(2)
print(GLOBAL_LIST)
