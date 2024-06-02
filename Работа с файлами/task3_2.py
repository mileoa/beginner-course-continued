import random

numbers = []
for i in range(random.randint(1, 10)):
    numbers.append(random.randint(1, 10))

path = "./task3_1/"

def sum_numbers_from_file(fi):
    sum = 0
    line = fi.readline()
    line_count = 0
    while line != '':
       sum += int(line.rstrip())
       line = fi.readline()
       line_count += 1
    if line_count != 3:
        raise Exception
    return sum

def sum_numbers_from_files(file_names, path):
    try:
        sum = 0
        for i in file_names:
            with open(path + str(i) + ".txt", 'r') as fi:
                sum += sum_numbers_from_file(fi)
        return sum
    except Exception:
        print("Произошла ошибка.")
        return

print(numbers)
print(sum_numbers_from_files(numbers, path))
