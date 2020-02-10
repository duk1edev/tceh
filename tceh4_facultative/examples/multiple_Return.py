

def find_min_max(number):
    min_num = min(number)
    max_num = max(number)
    return min_num, max_num


# Error find the error
maximum, minimum = find_min_max([1, 23, 43, 32])

print(maximum, minimum)