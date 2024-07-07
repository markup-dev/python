class WordsFinder:
	def __init__(self, *files):
		self.file_names = [*files]

	def get_all_words(self):
		all_words = {}
		words = []
		word = ''
		for file in self.file_names:
			with open(file, 'r', encoding='utf-8') as f:
				for line in f:
					line_list = line.lower().split()
					for line_word in line_list:
						for char in line_word:
							if char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
								continue
							else:
								word += char
						words.append(word)
						word = ''
					all_words[file] = words
		return all_words

	def find(self, word):
		for name, words in self.get_all_words().items():
			if word.lower() in words:
				return {name: words.index(word.lower()) + 1}

	def count(self, word):
		for name, words in self.get_all_words().items():
			return {name: words.count(word.lower())}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
