first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result = [len(len_) for len_ in first_strings if len(len_) > 5]
second_result = [(word, word2) for word in first_strings for word2 in second_strings if len(word) == len(word2)]
third_result = {word1: len(word1) for word1 in (first_strings + second_strings) if not len(word1) % 2}


print(first_result)
print(second_result)
print(third_result)