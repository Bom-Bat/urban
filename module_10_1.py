from time import sleep
from datetime import datetime
from threading import Thread


def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.truncate(0)
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово №{i}\n')
            sleep(0.1)
        return print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end = datetime.now()
time1 = time_end - time_start
print(time1)

time_start = datetime.now()
thr_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=wite_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_end = datetime.now()
time2 = time_end - time_start
print(time2)
timer = time1 - time2
print(f'Метод потоков выполнил задачу на {timer}с быстрее')