'''
DOCS : https://docs.python.org/3/library/re.html

'''

import re


def find_pattern(pattern, text):
    return re.search(pattern, text)

def find_all_pattern(pattern, text):
    return re.findall(pattern, text)

def gather_all_pattern(pattern, text):
    return re.finditer(pattern, text)

def change_all_pattern2target(pattern, target, text):
    return re.sub(pattern, target, text)


def remove_redundant_whitespaces(text):
    pattern = ' +'
    target  = ' '
    return change_all_pattern2target(pattern, target, text).strip()


if __name__ == '__main__':
    patterns = {'korean'  : r'[ㄱ-ㅎㅏ-ㅣ가-힣]+',
                'english' : r'[a-zA-Z]+',
                'number'  : r'[0-9]+',
                'weird'   : r'[^ㄱ-ㅎㅏ-ㅣ가-힣0-9a-zA-Z ]'}
    
    text = ' 0123  I am 신뢰에요  ~.~  @?@  #,#  3210 '

    # normalize
    text = change_all_pattern2target(patterns['weird'], '', text)
    text = remove_redundant_whitespaces(text)
    print(text); print()

    print(find_all_pattern(patterns['number'], text)); print()

    for pattern in gather_all_pattern(patterns['english'], text):
        print(pattern)
        print(pattern.group())
        print(pattern.span())
        print()
    
    '''print result
    0123 I am 신뢰에요 3210

    ['0123', '3210']

    <re.Match object; span=(5, 6), match='I'>
    I
    (5, 6)

    <re.Match object; span=(7, 9), match='am'>
    am
    (7, 9)

    '''