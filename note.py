from datetime import datetime


class Note:

    def __init__(self, ident, title, body):
        self.ident = ident
        self.title = title
        self.body = body
        self.date = str(datetime.now())

    def get_ident(self):
        return self.ident

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_date(self):
        return self.date

    def print_note(self):
        return "ID: {}\nTitle: {}\n{}\n{}".format(self.ident, self.title, self.body, self.date)
