import os, time

directory = r"."  # os.getswd()
i = 0
j = 0
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(os.path.join(root, file))
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(os.path.join(root, file))
        parent_dir = os.path.dirname(os.path.join(root, file))
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
        i += 1
    j += 1
print(f'\033[031mВсего найдено {i} файлов, в {j} каталогах')