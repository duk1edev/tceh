# print (1 / 0)

# Basic try/except

try:
    print(1 / 0)
except:
    print('0!!')

try:
    print(1 / 0)
except Exception:
    print('0!!!')

# Catching specific exceptions
try:
    print(1 / 0)
except ZeroDivisionError:
    print('Exception!')


# Catching exception instance

try:
    print(1 / 0)
except ZeroDivisionError as e:
    print('Exception! Stop it!')
    print(e)

print('----------------------------------------')
# Mismatched exception will not be captured
try:
    d = {'key': 23}
    print(d['does not exist'])
except KeyError as e:               # ValueError was before
    print('This wont be called', e)

try:
    d = {'key': 23}
    print(d['does not exist'])
except KeyError as e:
    print("Got it ", e)

print('---------------------------------------')
# Raise exception
try:
    raise ValueError('Custom message')
except ValueError as e:
    print(e)

print('---------------------------------------')
# Multiple except blocks

try:
    raise ValueError()
except ZeroDivisionError:
    print('Divided by zero!')
except AttributeError:
    print('Key is missing!')
except Exception as ex:
    print('I dont know whats going on!')
    print(ex)


# try/except/else

try:
    print('Fine')
except KeyError:
    print('Nope.')
else:
    print('Else clause')
finally:
    print('Finally finally')

# try/except/finally

try:
    print(1 / 0)
except ZeroDivisionError:
    print('0!')
finally:
    print('I will be called in the end')

# try/except/else

try:
    print('try')
except ValueError:
    pass
else:
    print('else')
finally:
    print('finally')

try:
    raise ValueError()
finally:
    print('Finally')