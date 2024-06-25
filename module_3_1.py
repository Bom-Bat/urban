def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):

    tuple_ = tuple([len(string), string.upper(), string.lower()])
    count_calls()
    return tuple_


def is_contains(string, list_to_search):
    count_calls()
    return string in list_to_search


calls = 0
string = ' '
while string != '0':
    string = str(input('\n\tВедите строку (0 прервать): '))
    if string == '0':
        break
    print(f'\n\tВаша строка в кортеже: {string_info(string)}')
list_to_search = []
list_ = ' '
string = ' '
while string != '0':
    while list_ != '0':
        list_ = str(input('\n\tВедите слово - элемент списка без учета регистра (0 прервать): '))
        list_ = list_.lower()
        if list_ == '0':
            break
        list_to_search.append(list_)
    string = str(input('\n\tВведите искомое слово без учета регистра (1 повторить список 0 прервать): '))
    string = string.lower()
    if string == '0':
        break
    elif string == '1':
        list_ = ' '
        continue
    a = is_contains(string, list_to_search)
    if a:
        print(f'\n\tСлово найдено: {a}')
    else:
        print(f'\n\tСлово не найдено: {a}')
print(f'\n\tФункции вызывались: {calls} раз')