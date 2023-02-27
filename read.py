import json
import config


def read_from_json():
    with open(config.file_path, encoding='utf-8') as file:
        dictionary = json.load(file)
        return dictionary
