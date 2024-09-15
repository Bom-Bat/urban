import inspect


def count(self, word):
    count_dict = {}
    word = word.lower()
    for name, words in self.get_all_words().items():
        count_dict[name] = words.count(word)
    return count_dict


def introspection_info(obj):
    typ = type(obj)
    di = [attr for attr in dir(obj) if not attr.startswith('__')]
    if not di:
        di = 'Отсутствуют'
    met = [attr for attr in dir(obj) if attr.startswith('__')]
    if not met:
        met = 'Отсутствуют'
    fun = inspect.getmembers(obj, predicate=inspect.isfunction)
    if not fun:
        fun = 'Отсутствуют'
    mod = inspect.getmodule(obj)
    return (f'Объект: {obj} имеет:\nТип:{typ}, \nАтрибуты: {di}, \nМетоды: {met}, \nФункции: {fun},'
            f' \nПринадлежит модулю: {mod}.')


number_info = introspection_info(42)
print(number_info)
function_info = introspection_info(count)
print(function_info)