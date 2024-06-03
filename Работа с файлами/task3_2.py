import random
from typing import IO

def sum_numbers_from_file(fi: IO) -> list:
    try:
        file_sum: list = [0, 0]
        line: str = fi.readline()
        line_count: int = 0
        while line != '':
            file_sum[0] += int(line.rstrip())
            line = fi.readline()
            line_count += 1
        if line_count != 3:
            return [0, 2]
        return file_sum
    except Exception:
        return [0, 1]

def sum_numbers_from_files(file_names: list, path: str) -> list:
    try:
        files_sum: list = [0, 0]
        for i in file_names:
            with open(path + str(i) + ".txt", 'r', -1, "utf-8") as fi:
                sum_file: list = sum_numbers_from_file(fi)
            if sum_file[1] != 0:
                return [0, sum_file[1]]
            files_sum[0] += sum_file[0]
        return files_sum
    except Exception:
        return [0, 3]

numbers: list = []
for i in range(random.randint(1, 10)):
    numbers.append(random.randint(1, 10))

path: str = "./task3_1/"

print(numbers)
print(sum_numbers_from_files([], path))
