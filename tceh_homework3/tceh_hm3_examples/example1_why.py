data = [1, 2, 6.43, - 4, 0.4]

minimum = data[0]

for item in data:
    if item < minimum:
        minimum = item

print('Minimum is ', minimum)

# But

other_data = [-10, -23, -9, 0.12, 0.4, -1.4]

new_minimum = other_data[0]

def min_in_list(input_list):
    new_minimum = other_data[0]
    for item in input_list:
        if item < new_minimum:
            new_minimum = item
    # return new_minimum


print('Other min is', new_minimum) # min_in_list(other_data))
