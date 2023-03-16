# https://www.python.org/dev/peps/pep-0570/#logical-ordering
# Positional-only parameters also have the (minor) benefit of enforcing some logical order when
# calling interfaces that make use of them. For example, the range function takes all its
# parameters positionally and disallows forms like:

# range(stop=5, start=0, step=2)
# range(stop=5, step=2, start=0)
# range(step=2, start=0, stop=5)
# range(step=2, stop=5, start=0)

# at the price of disallowing the use of keyword arguments for the (unique) intended order:

# range(start=0, stop=5, step=2)
"""
Write a function that accept any sequence (list, string, tuple) of unique values, and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
import string
from typing import List


def custom_range(seq, stop, *args) -> List:
    if len(args) > 2:
        raise ValueError("Too many parameters")
    start = seq[0]
    step = 1
    if len(args) == 1:
        start = stop
        stop = args[0]
    if len(args) == 2:
        start = stop
        stop = args[0]
        step = args[1]
    if step == 0:
        raise ValueError("Step cannot be zero")
    if start not in seq or stop not in seq:
        raise ValueError("Parameters are not from the sequence")
    result = []
    element = start
    while (step > 0 and seq.index(element) < seq.index(stop)) or (step < 0 and seq.index(element) > seq.index(stop)):
        result.append(element)
        element = seq[seq.index(element) + step]
    return result


if __name__ == '__main__':
    print(custom_range(string.ascii_lowercase, "g", "p"))
