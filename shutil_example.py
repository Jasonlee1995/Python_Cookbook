import shutil


def move(src, dest):
    shutil.move(src, dest)

def copy_file(src, dest):
    shutil.copy2(src, dest)

def copy_tree(src, dest):
    shutil.copytree(src, dest, dirs_exist_ok=False)

def remove_tree(dir):
    shutil.rmtree(dir)


if __name__ == '__main__':
    src_dir  = '/put/your/source/directory'
    dest_dir = '/put/your/destination/directory'
    rm_dir   = '/put/your/directory/to/remove'
    
    # move(src_dir, dest_dir)
    # copy_file(src_dir, dest_dir)
    # copy_tree(src_dir, dest_dir)
    # remove_tree(rm_dir)