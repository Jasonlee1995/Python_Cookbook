import glob


def find_all(target):
    return glob.glob(target, recursive=False)


if __name__ == '__main__':
    target = './**/**/*.txt'
    print(find_all(target))

    '''print result
    ['./temp/a/3.txt', './temp/a/2.txt', './temp/a/1.txt', './temp/b/1.txt']
    '''