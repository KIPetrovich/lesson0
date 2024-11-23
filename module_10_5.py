import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line)
        file.close()

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = datetime.datetime.now()
    for name in filenames:
        read_info(name)
    print(datetime.datetime.now() - start_time, '(линейный)')

    start_time = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    print(datetime.datetime.now() - start_time, '(многопроцессный)')

