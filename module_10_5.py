import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        print(name)
        for _ in enumerate(file):
            lin = file.readline()
            all_data.append(lin)
        return print(all_data)


list_file = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
#time_start = datetime.now()
#list_ = [read_info(name) for name in list_file]


if __name__ == '__main__':
    time_start = datetime.now()
    with multiprocessing.Pool(processes=5) as pool:
        pool.map(read_info, list_file)
    time_end = datetime.now()
    time1 = time_end - time_start
    print(time1)
#0:00:04.562027 время линецного выполнения
#0:00:02.598584 время мультипроцесерного выполнения