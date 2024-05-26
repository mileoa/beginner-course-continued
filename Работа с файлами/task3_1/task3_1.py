import random

def fill_file_3random_numbers(fi):
    try:
        for j in range(3):
            fi.write(str(random.randint(-1000, 1000)) + "\n")
    except AttributeError:
        print("Передан параметр неверного типа.")
    except ValueError:
        print("Файл уже закрыт.")
    except Exception:
        print("Ошибка")

for i in range(10):
    with open(str(i + 1) + ".txt", 'w') as fi:
        fill_file_3random_numbers(fi)