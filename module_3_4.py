def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(f'\n\t{result1}')
print(f'\n\t{result2}')
list_ = ' '
list_to_search = []
a = input('\n\tВведите слово: ')
while list_ != '0':
    list_ = str(input('\n\tВедите слово - элемент списка без учета регистра (0 прервать): '))
    if list_ == '0':
        break
    list_to_search.append(list_)
result3 = single_root_words(a,*list_to_search)
print(f'\n\t{result3}')