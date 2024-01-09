'''
DOCS : https://docs.python.org/3/library/difflib.html

'''

import difflib


def match_info(hyp, ref):
    '''
    '- ' : line unique to sequence 1
    '+ ' : line unique to sequence 2
    '  ' : line common to both sequences
    '? ' : line not present in either input sequence

    '''
    hyp_match, ref_match = [], []
    for info in difflib.ndiff(hyp, ref):
        if   info.startswith('- '):
            hyp_match.append(False)
        elif info.startswith('+ '):
            ref_match.append(False)
        elif info.startswith('  '):
            hyp_match.append(True)
            ref_match.append(True)

    return hyp_match, ref_match


if __name__ == '__main__':
    hyp = 'I lik piazza.'.split()
    ref = 'I like pizza!'.split()

    hyp_match, ref_match = match_info(hyp, ref)

    print(list(difflib.ndiff(hyp, ref)))
    print()

    print(hyp)
    print(hyp_match)
    print(ref)
    print(ref_match)
    
    '''print result
    ['  I', '- lik', '+ like', '?    +\n', '- piazza.', '?   -   ^\n', '+ pizza!', '?      ^\n']

    [ 'I',  'lik', 'piazza.']
    [True,  False,     False]
    [ 'I', 'like',  'pizza!']
    [True,  False,     False]
    '''