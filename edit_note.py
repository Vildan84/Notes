import config
import note
import os.path
import read
import write
import delete_note


def edit_body(ident, text):

    if os.path.exists(config.file_path):
        dictionary = read.read_from_json()
        for item in dictionary['notes']:
            if item['id'] == ident:
                temp_note = note.Note(item['id'], item['title'], text)
                write.write_to_json(temp_note)
                delete_note.delete(ident)
                break

        else:
            print("Неверный ID заметки")

    else:
        print("Файл не найден")


def edit_title(ident, text):

    if os.path.exists(config.file_path):
        dictionary = read.read_from_json()
        for item in dictionary['notes']:
            if item['id'] == ident:
                temp_note = note.Note(item['id'], text, item['body'])
                write.write_to_json(temp_note)
                delete_note.delete(ident)
                break

        else:
            print("Неверный ID заметки")

    else:
        print("Файл не найден")
