import json
import note
import read
import os.path
import config


def write_to_json(n: note.Note):

    if os.path.exists(config.file_path):
        data = read.read_from_json()
        mydict = {"id": n.get_ident(), "title": n.get_title(), "body": n.get_body(), "date": n.get_date()}
        data["notes"].append(mydict)

        with open("data.json", "w", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    else:
        mydict = {"notes": [{"id": n.get_ident(), "title": n.get_title(), "body": n.get_body(), "date": n.get_date()}]}
        with open("data.json", "w", encoding='utf-8') as f:
            json.dump(mydict, f, ensure_ascii=False, indent=2)

