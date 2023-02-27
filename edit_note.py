import config
import note
import os.path
import read
import write
import delete_note


def edit(ident, text):

    if os.path.exists(config.file_path):
        dictionary = read.read_from_json()
        for item in dictionary['notes']:
            if item['id'] == ident:
                temp_note = note.Note(item['id'], item['title'], text)
                write.write_to_json(temp_note)
                delete_note.delete(ident)
            else:
                print("Неверный ID заметки")
            break
    else:
        print("Файл не найден")
