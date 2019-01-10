from entry_urls import EntryURLs
from dump_entries import DumpEntries

print(r"""
 ____
/\  _`\
\ \ \L\ \ __   _____   __  __    ____
 \ \ ,__/'__`\/\ '__`\/\ \/\ \  /',__\
  \ \ \/\  __/\ \ \L\ \ \ \_\ \/\__, `\
   \ \_\ \____\\ \ ,__/\/`____ \/\____/
    \/_/\/____/ \ \ \/  `/___/> \/___/
                 \ \_\     /\___/
                  \/_/     \/__/

This script will:

- Fetch an index of each of Samuel Pepys' diary entries
  from pepysdiary.com's public API
- Fetch each individual diary entry from the public API
- Parse each diary entry from HTML into text, removing
  links and references (it will wait half a second between
  requests in order to not tax the API)
- Store the entries and metadata as JSON
""")

entry_urls = EntryURLs().entry_urls
entries = DumpEntries(entry_urls)
