def my_function():
    print('I am a function!')


print('Functions are objects, ', isinstance(my_function, object))

test = my_function()
test


# You can pass functions as parameters

def call_passed_function(incoming):
    print('Calling')
    incoming()
    print('Called')


call_passed_function(my_function)


# You can not call uncallable things:

try:
    d = 2
    d()
except TypeError as e:
    print('It is not a function', e)


# You can check if something could be called:
print(callable(123), callable(print), callable(len), callable('str'))

# You can return function from a function


def return_min_function():
    return min


test = return_min_function()
min_value = test(4, 55, -9, 433)
print('Min value is ', min_value)
