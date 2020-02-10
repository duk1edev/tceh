def noname_func(*args: str, glue=":"):
    str_list = []
    for item in args:
        if len(item) > 3:
            # str_list.append(item)
            print(item + glue, end='')
    return str_list


print(noname_func('ASAMA', 'sds', 'shads', 'deeded', 'cc'))
