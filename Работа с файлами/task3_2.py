import random

first_number = random.randint(1, 10)
second_number = random.randint(1, 10)
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

def sum_numbers_from_files(first_number, second_number, path):
    try:
        fi1 = open(path + str(first_number) + ".txt", 'r')
        fi2 = open(path + str(second_number) + ".txt", 'r')
        return sum_numbers_from_file(fi1) + sum_numbers_from_file(fi2)
    except Exception:
        print("Произошла ошибка.")
        return
    finally:
        fi1.close()
        fi2.close()

print(sum_numbers_from_files(first_number, second_number, path))
