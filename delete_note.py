import config
import json
import os.path
import read


def delete(ident):

    if os.path.exists(config.file_path):
        dictionary = read.read_from_json()
        for item in dictionary['notes']:
            if item['id'] == ident:
                dictionary['notes'].remove(item)
                with open("data.json", "w", encoding='utf-8') as f:
                    json.dump(dictionary, f, ensure_ascii=False, indent=2)
            else:
                print("Неверный ID заметки")
            break
    else:
        print("Файл не найден")