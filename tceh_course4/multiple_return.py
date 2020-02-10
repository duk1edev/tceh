def find_min_max(data):
    min_num = min(data)
    max_num = max(data)

    return min_num, max_num


minimum, maximum = find_min_max([123, 32, -32, 12])
print(minimum, maximum)