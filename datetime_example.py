'''
DOCS : https://docs.python.org/3/library/datetime.html

'''

import datetime as dt


def str2datetime(str_input, str_format):
    return dt.datetime.strptime(str_input, str_format)

def datetime2str(dt_input, str_format):
    return dt.datetime.strftime(dt_input, str_format)

def add_time(dt_input, days_to_add):
    return dt_input + dt.timedelta(days=days_to_add)


if __name__ == '__main__':
    today = '2024.01.01'
    str_format = '%Y.%m.%d'

    today_dt = str2datetime(today, str_format)
    after_100_dt = add_time(today_dt, 100)
    after_100 = datetime2str(after_100_dt, str_format)

    print(f'{today}\t{today_dt}')
    print(f'{after_100}\t{after_100_dt}')

    '''print result
    2024.01.01      2024-01-01 00:00:00
    2024.04.10      2024-04-10 00:00:00
    '''