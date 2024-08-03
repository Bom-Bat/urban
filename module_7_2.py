def custom_write(file_name, strings):
    strings_positions = {}
    j = 1
    file = open(file_name, 'a', encoding='utf-8')
    file.seek(0)
    with open(f'{file_name}', 'w'):
        pass
    for i in strings:
        a = file.tell()
        file.write(f'{i}\n')
        strings_positions[(j, a)] = f'{i}'
        j += 1
    file.close()
    if file.closed: print(f'{file_name} - файл закрыт!')
    return strings_positions


info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
