'''
DOCS : https://docs.python.org/3/library/unicodedata.html

General category of character can be find in wiki
https://en.wikipedia.org/wiki/Unicode_character_property

'''


import unicodedata


def gather_text_info(text):
    info = {}
    for c in text:
        category = unicodedata.category(c)
        if category not in info:
            info[category] = []
        info[category].append(c)
    return info

def normalize_text(form, text):
    '''
    form
      NFC  : canonical decomposition + canonical composition
      NFD  : canonical decomposition
      NFKC : compatibility decomposition + canonical composition
      NFKD : compatibility decomposition
    '''
    return unicodedata.normalize(form, text)


if __name__ == '__main__':
    forms = ['NFC', 'NFD', 'NFKC', 'NFKD']
    text  = '㉮㈎가 ⓐ⒜a ①⑴1'

    print(gather_text_info(text))
    print()
    
    print('Original', len(text))
    print(text)
    print()

    for form in forms:
        print(form, len(normalize_text(form, text)))
        print(normalize_text(form, text))
        print()

    '''print result
    {'So': ['㉮', '㈎', 'ⓐ', '⒜'], 'Lo': ['가'], 'Zs': [' ', ' '], 'Ll': ['a'], 'No': ['①', '⑴'], 'Nd': ['1']}

    Original 11
    ㉮㈎가 ⓐ⒜a ①⑴1

    NFC 11
    ㉮㈎가 ⓐ⒜a ①⑴1

    NFD 12
    ㉮㈎가 ⓐ⒜a ①⑴1

    NFKC 17
    가(가)가 a(a)a 1(1)1

    NFKD 20
    가(가)가 a(a)a 1(1)1

    '''