def this_functions_print_stars():
    print('I will print stars!')
    print('**********')


this_functions_print_stars()


# Step 1
def my_function(input_var1, input_var2):
    print(input_var1, input_var2)
    return input_var1 + input_var2


first_call = my_function(1, 1)
print(first_call)

second_call = my_function(1, 321)
print(second_call)


# Step 2
def my_function(var1, var2, var3):
    print('No way I am using this: {}, {}, {}'.format(var1, var2, var3))


new_call = my_function((1, 2, 3, 4), 'second', 3.23)
print(new_call)


# Step 3
def function_with_default_value(name, age=0, needs_stars=False):
    message = '{} is {} years old!'.format(name, age)
    print(message)

    if needs_stars:
        print('*********')


function_with_default_value('Vitalii')
function_with_default_value('Vitalii', 27)
function_with_default_value('Vitalii', 27, True)


# Step 4
def name_values(name=None, surname=None, patronimic=None):
    print('Full name: {} {} {}'.format(surname, name, patronimic))


name_values('Vitalii', 'Antonov', 'Olegovich')
name_values(surname='Antipov', name='Osad', patronimic='Kocharocsda')
name_values(surname='Osadochick', patronimic='Ogyrcovich', name='Pen`ok')


# Complex examples

# Complex step 1:
def sum_all(*args):
    print(args, type(args))

    result = 0
    for arg in args:
        result += arg
    return result


my_list = [123, 323, 123, 312, 3123]

print(sum_all(13213, 123, 32, 1, 23, 124, 5, 516, 36))
# print(sum_all(my_list))


# Complex step 2:
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


n = 5
print('Factorial {} = {}'.format(n, factorial(n)))


# Complex step 3:
def do_callback(function, argument):
    return function(argument)


result = do_callback(len, 'length string')
print(result)

# Complex step 4
def all_together(value, *args, **kwards):
    message = kwards.pop('message', 'default message')
    if value > sum(args):
        print(message)
    else:
        print('value is not bigger that sum(args)')


all_together(1, 0)
all_together(1, 32, 3, 6)
all_together(43, 1, 3, 4, 5, message='Done!!!!!')


# Complex step 5:
def enclosing(value):
    def _inner():
        print('value: {value}, new_value: {new_value}'.format(
            new_value=new_value, value=value))

    new_value = str(value * 10) * 2
    _inner()
    return new_value


enclosing(25)


# Complex step 6:
def decorator(function):
    def _inner(value):
        print(function(value))

    print('called')
    return _inner


decorated = decorator(len)
decorated([1, 2, 3])
