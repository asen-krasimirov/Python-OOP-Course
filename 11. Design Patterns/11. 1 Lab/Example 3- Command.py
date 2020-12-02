import sys


class Window:
    @staticmethod
    def exit():
        sys.exit(0)


class Document:

    def __init__(self, filename):
        self.filename = filename
        self.contents = 'This file cannot be modified'

    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.contents)


class ToolbarDocument:

    def __init__(self, name, iconname, command):
        self.name = name
        self.iconname = iconname
        self.command = command

    def click(self):
        self.command.execute()


class SaveCommand:

    def __init__(self, document):
        self.document = document

    def execute(self):
        self.document.save()


class ExitCommand:

    def __init__(self, window):
        self.window = window

    def execute(self):
        self.window.exit()


if __name__ == '__main__':
    test_document = Document('file.txt')
    toolbar = ToolbarDocument('test', 'icon123', SaveCommand(test_document))
    toolbar.click()
