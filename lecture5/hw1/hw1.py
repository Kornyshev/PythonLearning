"""
We have a file that works as key-value storage,
each line is represented as key and value separated by = symbol, example:

name=kek
last_name=top
song_name=shadilay
power=9001

Values can be strings or integer numbers.
If a value can be treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt')
That has its keys and values accessible as collection items and as attributes.

Example:
storage['name']     # will be string 'kek'
storage.song        # will be 'shadilay'
storage.power       # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute
(for example when there's a line `1=something`) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.
"""

from key_value_storage import KeyValueStorage

if __name__ == '__main__':
    storage = KeyValueStorage('task1.txt')
    print(storage['name'])
    print(storage.song)
    print(storage.new_value)
    print('-' * 15)

    for k, v in storage:
        print(f'Pair: {k} = {v}. Key type: {type(k)}, Value type: {type(v)}')
    print('-' * 15)
    print([f'Int pair: {key} = {value}.' for key, value in storage if type(value) is int])
    print('-' * 15)

    storage['key_from_code'] = 42
    storage['new_string_from_code'] = 'Some String'
    for k, v in storage:
        print(f'Pair: {k} = {v}. Key type: {type(k)}, Value type: {type(v)}')
