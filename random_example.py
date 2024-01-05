'''
DOCS : https://docs.python.org/3/library/random.html

'''

import random


def sample_single_int(start, stop, step=1):
    # randomly element from range(start, stop, step)
    return random.randrange(start, stop, step)

def sample_single_uniform(start, stop):
    # random floating point number N such that start <= N <= stop
    return random.uniform(start, stop)

def sample_single(seq):
    # random element from seq
    return random.choice(seq)

def sample_multi_with_replacement(seq, sample_num):
    return random.choices(seq, k=sample_num)

def sample_multi_without_replacement(seq, sample_num):
    return random.sample(seq, k=sample_num)


if __name__ == '__main__':
    start, stop, step = 10, 13, 2
    print(list(range(start, stop, step)))
    print(sample_single_int(start, stop, step))
    print(sample_single_uniform(start, stop))
    print()

    seq = ['a', 'b', 'c']
    sample_num = 3
    print(sample_single(seq))
    print(sample_multi_with_replacement(seq, sample_num))
    print(sample_multi_without_replacement(seq, sample_num))

    '''print result (result may differ cause of randomness)
    [10, 12]
    12
    11.813542335705899

    a
    ['a', 'b', 'b']
    ['b', 'a', 'c']
    '''