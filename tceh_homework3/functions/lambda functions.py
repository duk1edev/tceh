# Map
from functools import reduce


def work(value):
    return value * 2


t = [1, 2, 10]
m = list(map(work, t))
print(m)


# The same, but using lambda function
m1 = map(lambda x: x * 3, t)
print(list(m1))


# fitler

print(list(filter(lambda v: v > 0, [-1, -2, -3, 23, 32])))

# reduce

r = [1, 4, 2, 3]

result = reduce(lambda x, y: x + y,r)
print(result)