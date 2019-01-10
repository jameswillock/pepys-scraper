import unittest
from format_entry_content import FormatEntryContent

class TestFormatEntryContent(unittest.TestCase):
	def format(self, string):
		return FormatEntryContent(string).format()

	def test_removes_superscript(self):
		string = self.format('<p>Hello<sup>1</sup></p>')
		self.assertEqual(string, 'Hello')

	def test_removes_links(self):
		string = self.format('<p>Hello <a href="/">world</a></p>')
		self.assertEqual(string, 'Hello world')

if __name__ == '__main__':
	unittest.main()
