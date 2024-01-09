'''
DOCS : https://docs.python.org/3/library/csv.html

'''

import csv


def read_csv(csv_path):
    '''
    read csv and print each line
    '''
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)

def write_csv(csv_path, dummy_info):
    '''
    write csv with dummy info
    '''
    with open(csv_path, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        for line in dummy_info:
            csv_writer.writerow(line)

def append_csv(csv_path, dummy_info):
    '''
    append csv with dummy info
    '''
    with open(csv_path, 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        for line in dummy_info:
            csv_writer.writerow(line)


if __name__ == '__main__':
    csv_path   = '/put/your/csv/path/'
    dummy_info = [['Test', 'purpose'], [None, None]]
    
    # read_csv(csv_path)
    # write_csv(csv_path, dummy_info)
    # append_csv(csv_path, dummy_info)