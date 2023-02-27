import click
import note
import read
import write
import time
import list_notes
import os.path
import config
import edit_note
import delete_note


@click.group()
def main():
    """Это простое приложение заметки"""
    pass


@click.command()
@click.option("--title", "-t", default="Заметка", help="Добавление заголовка к заметке")
@click.option("--msg", "-m", default="Пустой текст", help="Основное тело заметки")
def add(title, msg):

    ident = time.strftime("%m%d%H%M%S", time.localtime())
    my_note = note.Note(ident, title, msg)
    write.write_to_json(my_note)


@click.command()
@click.argument("ident")
@click.option("--body", "-b", help="Изменение текста заметки")
def edit(ident, body):
    edit_note.edit(ident, body)


@click.command()
@click.argument("ident")
def delete(ident):
    delete_note.delete(ident)


@click.command()
def list():

    if os.path.exists(config.file_path):
        dictionary = read.read_from_json()
        list_notes.list_of_notes(dictionary)
    else:
        click.echo("Файл не найден")


main.add_command(list)
main.add_command(add)
main.add_command(edit)
main.add_command(delete)


if __name__ == '__main__':
    main()
