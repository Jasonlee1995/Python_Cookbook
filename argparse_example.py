'''
DOCS : https://docs.python.org/3/library/argparse.html

'''

import argparse


parser = argparse.ArgumentParser(description='Test')
parser.add_argument('description',    type=str)
parser.add_argument('-a', '--apple',  type=int, default=0)
parser.add_argument('-b', '--banana', type=int, default=0)
parser.add_argument('-c', '--candle', type=int, choices=range(1, 4), required=True)
parser.add_argument('-s', '--save',   action='store_true')
args = parser.parse_args()


if __name__ == '__main__':
    print(args)
    print()

    for key in vars(args):
        print(key, vars(args)[key])
    

    '''print result of "python argparse_example.py test -c 2"
    Namespace(description='test', apple=0, banana=0, candle=2, save=False)

    description test
    apple 0
    banana 0
    candle 2
    save False
    '''