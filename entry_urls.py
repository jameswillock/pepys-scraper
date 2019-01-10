import time
import requests
from progress.bar import Bar


class EntryURLs:
    def __init__(self):
        self.entry_urls = []
        self.current_page_url = 'https://www.pepysdiary.com/api/v1/entries?page=1'
        self.bar = None
        self.__scrape(True)

    def __entries(self):
        return requests.get(self.current_page_url).json()

    def __scrape(self, first_run=False):
        entries = self.__entries()

        if first_run:
            total_pages = int(entries['totalPages'])
            self.bar = Bar('Fetching pages', max=total_pages)

        for entry in entries['results']:
            self.entry_urls.append(entry['apiURL'])

        self.bar.next()

        if entries['nextPageURL'] is not None:
            time.sleep(0.5)
            self.current_page_url = entries['nextPageURL']
            self.__scrape(False)
        else:
            self.bar.finish()

        return True
