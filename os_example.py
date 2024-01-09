'''
DOCS : https://docs.python.org/3/library/os.html

'''

import os


def get_files_list(target_path):
    return os.listdir(target_path)

def check_path_exist(target_path):
    return os.path.exists(target_path)

def make_tree(target_path):
    os.makedirs(target_path)

def print_tree(target_path):
    for (root_dir, folders, files) in os.walk(target_path):
        print(root_dir, folders, files)


if __name__ == '__main__':
    base_dir = './test'
    target_paths = ['a/1', 'a/2', 'a/3', 'b/1']
    for target_path in target_paths:
        target_path = os.path.join(base_dir, target_path)
        if not check_path_exist(target_path):
            make_tree(target_path)

    print_tree(base_dir)

    '''print result
    ./test ['a', 'b'] []
    ./test/a ['1', '3', '2'] []
    ./test/a/1 [] []
    ./test/a/3 [] []
    ./test/a/2 [] []
    ./test/b ['1'] []
    ./test/b/1 [] []
    '''