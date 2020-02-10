

simple_tuple = (1, 2, 3, 4, 5)
print(simple_tuple)

simple_tuple += (6, )
print(simple_tuple)

# empty tuple
new_tuple = tuple()

empty_tuple  = tuple()
tuple1 = (1, )
tuple2 = (1, )
not_a_tuple = (1)

print(
    tuple1 == tuple2,
    tuple2 == not_a_tuple,
    type(not_a_tuple),
    not_a_tuple
)
print((1, 2) == (1, 2, ))



# tuple operations

# add
tuple1 = tuple1 + tuple2
print(tuple1)

print(1 in tuple1, 2 in tuple1)

tuple1 = (2, ) + tuple1 + (not_a_tuple, )

print("lenth: ", len(tuple1), len(tuple2), len(empty_tuple))
print(tuple2[0], tuple1[0:2], tuple1[:-1])
print(tuple1)


# removing

tuple1 = (1, 2, 'string', 'one more')
new_tuple = tuple()

for item in tuple1:
    if not isinstance(item, str):
        new_tuple += (item, )
print(new_tuple)