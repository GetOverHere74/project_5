import json
from datetime import datetime

def loading_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as loaded_file:
        return json.load(loaded_file)

def filtered_list(loaded_file):
    json_adjective = list(filter(lambda x: len(x) and x['state'] == 'EXECUTED', loaded_file))
    return json_adjective

def sort_by_date(json_adjective):
    sorted_list = sorted(json_adjective,key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return sorted_list
