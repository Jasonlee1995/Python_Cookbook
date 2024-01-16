'''
DOCS : https://docs.python.org/3/library/collections.html

'''

import collections


def make_counter(lst):
    return collections.Counter(lst)

def get_most_common(counter, num):
    return counter.most_common(num)

def mathematical_operation(counterA, counterB, operation):
    if operation == 'add':          return counterA + counterB
    if operation == 'subtract':     return counterA - counterB
    if operation == 'intersection': return counterA & counterB
    if operation == 'union':        return counterA | counterB
    raise ValueError('Unknown Operation')


if __name__ == '__main__':
    abc_lst = ['a', 'a', 'a', 'b', 'c', 'c']
    ab_lst  = ['a', 'a', 'b']

    abc_cnt = make_counter(abc_lst)
    ab_cnt  = make_counter(ab_lst)

    print(abc_cnt, get_most_common(abc_cnt, 1))
    print(ab_cnt, get_most_common(ab_cnt, 1))
    print(mathematical_operation(abc_cnt, ab_cnt, 'subtract'))

    '''print result
    Counter({'a': 3, 'c': 2, 'b': 1}) [('a', 3)]
    Counter({'a': 2, 'b': 1}) [('a', 2)]
    Counter({'c': 2, 'a': 1})
    '''