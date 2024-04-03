import json
from datetime import datetime

def loading_file(file_name):
    """Функция загружает файл и возвращает его в виде списка"""
    with open(file_name, 'r', encoding='utf-8') as loaded_file:
        return json.load(loaded_file)

def filtered_list(loaded_file):
    """Функция фильтрует список в соответствии с фильтрами"""
    json_adjective = list(filter(lambda x: len(x) and x['state'] == 'EXECUTED', loaded_file))
    return json_adjective

def sort_by_date(json_adjective):
    """Функция сортирует список в соответствии с фильтрами"""
    sorted_list = sorted(json_adjective,key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return sorted_list

def date_format(date):
    """Функция форматирует дату в соответствии с фильтрами"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"

def get_card_number(card):
    """Функция формирует номер карты или счета в соответствии с фильтрами"""
    req = card.split()
    if req[0] == 'Счет':
        return 'Счет **' + card[-4:]
    else:
        card_name = ' '.join(req[:-1])
        return card_name + ' ' + req[-1][:4] + ' ' + req[-1][4:6] + '** ****' + req[-1][-4:]

def get_summ(money):
    """Функция формирует сумму в соответствии с фильтрами"""
    return f'{money['operationAmount']["amount"]} {money["operationAmount"]["currency"]["name"]}'

def load_main(num_operations=5):
    """Функция выводит операцию в нужном формате """
    loaded_file = loading_file('operations.json')
    json_adjective = filtered_list(loaded_file)
    sorted_list = sort_by_date(json_adjective)
    for operation in sorted_list:
        if num_operations == 0:
            break
        print(date_format(operation["date"]), operation["description"])
        if operation["description"] != "Открытие вклада":
            print(get_card_number(operation["from"]), " -> ", end='')
        print(get_card_number(operation["to"]))
        print(get_summ(operation),'\n')
        num_operations -= 1

load_main()
