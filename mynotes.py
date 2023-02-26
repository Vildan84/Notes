import click
import note
import write
import time


@click.command()
@click.option('--title', '-t', default='Заметка', help='Добавляет заголовок к заметке')
@click.option('--msg', '-m', default="Пустой текст", help='Основное тело заметки')
# @click.option('--search', '-s', type=int, help='Для поиска заметки по ID')
def main(title, msg):
    """Это простое приложение заметки"""
    id_time = time.localtime()
    ident = time.strftime("%m%d%Y%H%M%S", id_time)
    my_note = note.Note(ident, title, msg)
    write.write_to_json(my_note)


if __name__ == '__main__':
    main()
