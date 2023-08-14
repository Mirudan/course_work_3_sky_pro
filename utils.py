import json
import os
from operator import itemgetter


def load_json(file_name):
    """
    Получаем массив операций
    :param file_name: путь к json файлу
    :return: массив не пустых словарей
    """
    with open(file_name, encoding='utf-8') as file:
        dict_json = json.load(file)

    new_dict = []
    for dict in dict_json:
        if dict:
            new_dict.append(dict)

    return new_dict


def get_list_executed(operation_list):
    """
    Получаем последние 5 выполненных операций
    :param operation_list: массив операций
    :return: последние 5 выполненных операций
    """

    exucuted_list = []
    for operation in operation_list:
        if operation['state'] == "EXECUTED":
            exucuted_list.append(operation)

    newlist = sorted(exucuted_list, key=itemgetter('date'), reverse=True)

    return newlist[0: 5]
