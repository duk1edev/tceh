# 1
list1 = [1, 23, 34, 2, 0, 43, 23, 4, 3, 3]
list1.sort()
print(list1)

# 2
dict = {6: '6', 7: "7", 8: '8'}
for key, value in dict.items():
    print(key, value)

# 3
tuple1 = (1.32, 3.323, 5.432, 1.234, 7.3123, 9.9544)
print('max = ', max(tuple1))
print('min = ', min(tuple1))

# 4
list_words = ['Earth', 'Russia', 'Moscow']
print(list_words[0] + ' -> ' + list_words[1] + ' -> ' + list_words[2])
print(" -> ".join(list_words))

# 5
str_adr = '/bin:/usr/bin:/usr/local/bin'
splited_str_adr = str_adr.split(':')
print(splited_str_adr)

# 6
list_num = [i for i in range(1, 100) if i % 7 == 0]
print(type(list_num), list_num)

# 7
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]
          ]
print('Print rows')
for col in range(len(matrix)):
    print('\n')
    for string in range(len(matrix[col])):
        print(matrix[col][string], end=' ')

print('Print columns')
for column in range(len(matrix) - 1):
    print('\n')
    for item in range(len(matrix[column])+1):
        print(matrix[item][column], sep=' ')


# 8
var = [1, 'fix', False, None, {1:'dict'}, (5, 6, 7), True]
for i in var:
    print(i, ' ', var.index(i))

# 9
some_data = ['to-delete', '1', 'to-delete', '2', '3', '4', 'to-delete', '5']
print('list before cleaning: ', some_data)
some_data = [data for data in some_data if data != 'to-delete']
print('list after cleaning: ', some_data)


