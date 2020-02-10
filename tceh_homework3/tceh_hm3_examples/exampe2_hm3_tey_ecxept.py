try:
    print(1 / 0)
except:
    print('0!!!')

try:
    print(1 / 0)
except Exception:
    print('0_1!!!!!')


try:
    print(1 / 0)
except ZeroDivisionError:
    print('Exception')

try:
    print(1 / 0)
except ZeroDivisionError as some_var:
    print('Exception! Stop it!')
    print(some_var)

# Mismatched exception will not be captured

try:
    d = {'key': 23}
    print(d['doesnt exist'])
except ZeroDivisionError:
    print('This wont be called!')

try:
    d = {'key': 23}
    print(d['does not exist!'])
except KeyError as e:
    print("Got it: ", e)

# Raising exception

try:
    raise ValueError('Custom message')
except ValueError as e:
    print('Message is ', e)

# Multiple except block

try:
    raise  ValueError()
except ZeroDivisionError:
    print('Divided by zero')
except AttributeError:
    print('Key is missing')
except Exception as ex:
    print("I don't know what's going on!")
    print(ex)

# Try/except/else:

try:
    print('Fine')
except KeyError:
    print('Nope.')
else:
    print('Else clause')

# Try/except/finally

try:
    print(1 / 0)
except ZeroDivisionError:
    print('0!!!!!')
finally:
    print('Finally will called in the end!')

# All together
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
