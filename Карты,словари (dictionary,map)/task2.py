import random
from typing import List, Dict

# Функция возвращает массив элементов, которые встретились в переданном массиве >= n раз.
def get_met_n(array: List[int], n: int) -> List[int]:
    # Считаем сколько раз встречается элемент.
    dcitionary: Dict[int, int] = {}
    result: List[int] = []
    for i in array:
        if i in dcitionary.keys():
            dcitionary[i] += 1
        else:
            dcitionary[i] = 1
        if dcitionary[i] >= n and i not in result:
            result.append(i)

    return result

# Заполняем массив случайными числами.
array: List[int] = []
for i in range(10):
    array.append(random.randint(1, 10))

print(array)
print(get_met_n(array, 0))
