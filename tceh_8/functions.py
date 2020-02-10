def work(value):
    return value * 2


t = [1, 2, 10, 44]
m = map(work, t)
print(list(m))

w = map(lambda x: x + 10, t)
print(list(w))


# filter

lst = [1, 2, 3, "on-delete", 5, 6, "on-delete"]

new_list = (filter(lambda x: x != 'on-delete', lst))

print(lst)
print(list(new_list))


# reduce

from  functools import reduce

r = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, r)
print(result)