from format_entry_content import FormatEntryContent
from progress.bar import Bar
import requests
import time
import json


class DumpEntries:
    def __init__(self, entry_urls):
        self.entry_urls = entry_urls
        self.__dump()

    def __entry(self, entry_url):
        return requests.get(entry_url).json()

    def __formatted_entry(self, entry):
        return FormatEntryContent(entry).format()

    def __entries(self):
        entries = []
        bar = Bar('Fetching entries', max=len(self.entry_urls))

        for entry_url in self.entry_urls:
            time.sleep(0.5)
            entry = self.__entry(entry_url)
            entries.append({
                'date': entry['date'],
                'title': entry['title'],
                'content': self.__formatted_entry(entry['entryHTML'])
            })
            bar.next()

        bar.finish()
        return entries

    def __dump(self):
        entries = self.__entries()

        with open('entries.json', 'w') as entries_file:
            json.dump({'entries': entries}, entries_file, indent=2)

        return True
