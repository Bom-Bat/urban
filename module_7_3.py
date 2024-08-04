class WordsFinder:
    file_names = []

    def __new__(cls, *f_n):
        cls.file_names = f_n
        return super().__new__(cls)

    def get_all_words(self):
        all_words ={}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                words_list = []
                for line in file:
                    line = line.lower()
                    symbols_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for symbol in symbols_to_remove:
                        line = line.replace(symbol, "")
                    words_list.extend(line.split())
                all_words[name] = words_list
        return all_words

    def find(self, word):
        find_dict ={}
        word = word.lower()
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if word == words[i]:
                    find_dict[name] = words.index(word) + 1
                    break
                else:
                    find_dict[name] = 0
        return find_dict

    def count(self, word):
        count_dict ={}
        word = word.lower()
        for name, words in self.get_all_words().items():
            count_dict[name] = words.count(word)
        return count_dict


finder2 = WordsFinder('test_file.txt')#, 'Walt Whitman - O Captain! My Captain!.txt',
                      # 'Rudyard Kipling - If.txt',
                      # 'Mother Goose - Monday’s Child.txt')
print(finder2.get_all_words()) # Все слова
word_w = input('Введите искомое слово: ')
print(finder2.find(word_w)) # 3 слово по счёту
print(finder2.count(word_w)) # 4 слова teXT в тексте всего