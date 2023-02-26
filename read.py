import json


def read_from_json():
    file_path = "./data.json"
    with open(file_path, encoding='utf-8') as file:
        dictionary = json.load(file)
        return dictionary
