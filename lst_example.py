def read_lst(lst_path):
    '''
    read lst and print each line
    '''
    with open(lst_path, 'r') as lst_file:
        lines = lst_file.readlines()
        for line in lines:
            print(line.rstrip('\n'))

def write_lst(lst_path, dummy_info):
    '''
    write lst with dummy info
    '''
    with open(lst_path, 'w') as lst_file:
        for line in dummy_info:
            lst_file.write(f'{line}\n')

def append_lst(lst_path, dummy_info):
    '''
    append lst with dummy info
    '''
    with open(lst_path, 'a') as lst_file:
        for line in dummy_info:
            lst_file.write(f'{line}\n')


if __name__ == '__main__':
    lst_path   = '/put/your/lst/path/'
    dummy_info = ['image_path, height, width',
                  'temp/a.png, 128, 256']
    
    # read_lst(lst_path)
    # write_lst(lst_path, dummy_info)
    # append_lst(lst_path, dummy_info)