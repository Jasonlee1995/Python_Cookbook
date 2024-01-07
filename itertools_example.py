'''
DOCS : https://docs.python.org/3/library/itertools.html

'''

import itertools


def accumulate_seq(seq):
    return itertools.accumulate(seq)

def combination_seq(seq, sample_num):
    return itertools.combinations(seq, sample_num)

def permutation_seq(seq, sample_num):
    return itertools.permutations(seq, sample_num)

def product_seqs(seqs):
    return itertools.product(*seqs)


if __name__ == '__main__':
    num_seq = [1, 3, 7]
    abc_seq = ['abc', 'de']
    sample_num = 2

    print(list(accumulate_seq(num_seq)))
    print(list(combination_seq(num_seq, sample_num)))
    print(list(permutation_seq(num_seq, sample_num)))
    print(list(product_seqs([num_seq, abc_seq])))

    '''print result
    [1, 4, 11]
    [(1, 3), (1, 7), (3, 7)]
    [(1, 3), (1, 7), (3, 1), (3, 7), (7, 1), (7, 3)]
    [(1, 'abc'), (1, 'de'), (3, 'abc'), (3, 'de'), (7, 'abc'), (7, 'de')]
    '''