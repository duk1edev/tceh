def logger(function):
    def inner(x, y):
        result = function(x, y)
        print("Result is, ")
        return result
    return inner


def sum(x, y):
    return x + y


def mul(x, y):
    return x * y


s = logger(sum)
s_result = s(5, 6)
print(s_result)

m = logger(mul)
m_result = m(2, 32)
print(m_result)