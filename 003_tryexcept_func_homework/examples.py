# Step 0:

def this_functions_prints_stars():
    print('I will print stars!')
    print('*********')


this_functions_prints_stars()


# Step 1
def my_function(input_var1, input_var2):
    print(input_var1, input_var2)
    return input_var1 + input_var2


first_call = my_function(1, 2)
print(first_call)

second_call = my_function(1, 123)
print(second_call)


# Step2
def my_function(var1, var2, var3):
    print('No way Im using this: {}, {}, {}'.format(var1, var2, var3))


new_call = my_function(1, 2, 3)
print(new_call)

# Step3
def sum_all(*numbers):
    print(numbers, type(numbers))
    sumo = 0
    for number in numbers:
        sumo += number
    return sumo


print(sum_all(1, 2, 3, 4))


def any_keywaords(**kwargs):
    print(kwargs)


any_keywaords(l=1, b=1, x=32)
