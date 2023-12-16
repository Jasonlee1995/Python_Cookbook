import json


def read_json(json_path):
    '''
    read json and print key & value
    if you have trouble, change 'encoding'
    '''
    with open(json_path, 'r') as json_file:
        dictionary = json.load(json_file)
        for key in dictionary:
            print(key, dictionary[key])

    return dictionary

    # with open(json_path, 'r', encoding='utf-8-sig') as json_file:
    #     dictionary = json.load(json_file)
    #     for key in dictionary:
    #         print(key, dictionary[key])

def write_json(json_path, dummy_info):
    '''
    write json with dummy info
    if you have trouble, change 'encoding' and 'ensure_ascii'
    '''
    with open(json_path, 'w') as json_file:
        json.dump(dummy_info, json_file, sort_keys=True, indent=4)
    
    # with open(json_path, 'w', encoding='utf-8-sig') as json_file:
    #     json.dump(dictionary, json_file, ensure_ascii=False, sort_keys=True, indent=4)

def append_json(json_path, dummy_info):
    '''
    append json with dummy info
    read json file -> update dummy_info -> save
    not a good way to append something on large json file
    if you have trouble, change 'encoding' and 'ensure_ascii'
    '''
    prev_json = read_json(json_path)
    prev_json.update(dummy_info)
    write_json(json_path, prev_json)


if __name__ == '__main__':
    json_path  = '/put/your/json/path/'
    dummy_info = {'key' : 'value'}
    
    # read_json(json_path)
    # write_json(json_path, dummy_info)
    # append_json(json_path, dummy_info)