def my_function():
    print('I am function')


print(my_function)
print('Functions are objects', isinstance(my_function, object))

test = my_function
test()

# You can do any actions with functions

my_list = []
my_list.append(my_function)
print(my_list)


# You can pass functions as parameters

def call_passed_functions(incoming):
    print('Calling')
    incoming()
    print('Called')


call_passed_functions(my_function)


# You can not call uncallable things:

try:
    d = 2
    d()
except TypeError as e:
    print('It is not a function', e)

# You can check if something could be called

print(callable(len), callable(45), callable(callable))

# You can return function from a function


def return_min_function():
    return min


test = return_min_function()
min_value = test(45, 34, 23, 12, -1554)
print('Min value: ', min_value)