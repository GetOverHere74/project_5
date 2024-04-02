import json

def loading_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as loaded_file:
        return json.load(loaded_file)
