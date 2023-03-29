# 1. Implement a function that flatten incoming data:
# non-iterables and elements from iterables (any nesting depth should be supported)
# function should return an iterator (generator function)
# don't use third-party libraries
# Example input:
# a = [1, 2, 3]
# b = 6
# c = 'zhaba'
# d = [[1, 2], [3, 4]]
# Output: 1 2 3 6 z h a b a 1 2 3 4
#
# 2. Implement a map-like function that returns an iterator (generator function).
# Extra functionality: if arg function can't be applied, return element as is + text exception
# Example input:
# a = [1, 2, 3]
# b = 6
# c = 'zhaba'
# d = True
# fun = lambda x: x[0]
# Output:
# 1
# 6: 'int' object is not subscriptable
# z
# True: 'bool' object is not subscriptable


def merge_elems(*elems):
    for elem in elems:
        if not hasattr(elem, '__iter__'):
            yield elem
        else:
            if isinstance(elem, str) and len(elem) == 1:
                yield elem
            else:
                yield from merge_elems(*elem)


def map_like(fun, *elems):
    for item in elems:
        try:
            yield fun(item)
        except (TypeError, IndexError) as e:
            yield f"{item}: {e}"


if __name__ == '__main__':
    a = 3
    b = 6
    bb = [4, 5]
    c = 'zha'
    d = [[1, 2], [3, ['fh', 'vn']]]
    e = {'a': ['y', 'u'], 'b': 2, 'c': 3}
    for _ in merge_elems(a, b, bb, c, d, e):
        print(_, end=' ')
    print('\n---------------')
    a = [1, 2, 3]
    b = 6
    c = 'zhaba'
    d = True
    fun1 = lambda x: x ** 2
    fun2 = lambda x: x[0]
    for _ in map_like(fun1, a, b, c, d):
        print(_)
    print('-' * 15)
    for _ in map_like(fun2, a, b, c, d):
        print(_)
