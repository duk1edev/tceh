# task1
my_list = [1, 3, 5, 2, 6, 9]
my_list.sort()
my_list.reverse()
print(my_list)

# task2
my_dict = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5'}
for key, value in my_dict.items():
    print(key, value)

# task3
my_tuple = (1, 3, 4, 7, 8, 10, 22)
print("Max = {}, Min = {}".format(max(my_tuple), min(my_tuple)))

# task4
word_list = ['Earth', 'Russia', 'Moscow']
print(word_list[0] + ' -> ' + word_list[1] + ' -> ' + word_list[2])

# task5
url = '/bin:/usr/bin:/usr/local/bin'
print(url.split(':'))

# taks6
for x in range(0, 100):
    if x % 7 == 0:
        print('{} - divided by 7'.format(x))
    else:
        print('{} - not divided by 7'.format(x))

# task7 - Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы
my_matrix = [
    [1, 2, 3, -1],
    [4, 5, 6, -2],
    [7, 8, 9, -3],
]
for row in my_matrix:
    print(row)

column1 = []
column2 = []
column3 = []
column4 = []
for item in my_matrix:
    column1.append(item[0])
    column2.append(item[1])
    column3.append(item[2])
    column4.append(item[3])

print('Столбец1: ', column1)
print('Столбец2: ', column2)
print('Столбец3: ', column3)
print('Столбец4: ', column4)

# task8 - Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс
obj_list = [1, None, 'str', 3.14, 566, False]
for item in obj_list:
    print(item, ": ", obj_list.index(item))

# taks9 - Cписок с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'
l = [23, 432, 231, 'to-delete', 'not-delete', 'to-delete', 342.3123, False, None]
for item in l:
    if item == 'to-delete':
        l.remove(item)
print(l)

for i in range(10, 0, -1):
    print(i)
