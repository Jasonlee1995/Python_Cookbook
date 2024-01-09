'''
DOCS : https://docs.python.org/3/library/zipfile.html

'''

import zipfile


def read_zip(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        zip_infos = zip_file.infolist()
        for zip_info in zip_infos:
            fname = zip_info.filename
            # # if weird character appears, use below
            # fname = zip_info.filename.encode("cp437").decode('utf-8')
            print(fname)

def extract_certain(zip_path, save_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        zip_infos = zip_file.infolist()
        for zip_info in zip_infos:
            fname = zip_info.filename
            # # if weird character appears, use below
            # fname = zip_info.filename.encode("cp437").decode('utf-8')

            # put your own logic
            if fname.endswith('.txt'):
                zip_file.extract(zip_info, path=save_dir)


if __name__ == '__main__':
    zip_path = '/put/your/zip/path/'
    # read_zip(zip_path)