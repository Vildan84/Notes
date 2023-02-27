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
@click.help_option("--title", "-t", help="Добавление и изменение заголовка к заметке")
@click.help_option("--msg", "-m", help="Добавление и изменение текста к заметке")
def main():
    """Simple app Notes"""
    pass


@click.command()
@click.option("--title", "-t", default="Заметка")
@click.option("--msg", "-m", default="Пустой текст")
def add(title, msg):
    ident = time.strftime("%m%d%H%M%S", time.localtime())
    my_note = note.Note(ident, title, msg)
    write.write_to_json(my_note)


@click.command()
@click.argument("ident")
@click.option("--msg", "-m")
@click.option("--title", "-t")
def edit(ident, msg, title):
    if msg and title:
        edit_note.edit_body(ident, msg)
        edit_note.edit_title(ident, title)
    elif title:
        edit_note.edit_title(ident, title)
    else:
        edit_note.edit_body(ident, msg)


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
