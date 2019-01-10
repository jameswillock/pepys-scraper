from bs4 import BeautifulSoup


class FormatEntryContent:
    def __init__(self, content):
        self.formatter = BeautifulSoup(content, 'html.parser')

    def format(self):
        [sup.extract() for sup in self.formatter('sup')]
        return self.formatter.get_text()
