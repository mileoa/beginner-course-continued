import random
from typing import List, Dict


# Функция возвращает массив элементов, которые встретились в переданном массиве >= n раз.
def get_met_n(array: List[int], n: int) -> List[int]:
    # Считаем сколько раз встречается элемент.
    elements_amount: Dict[int, int] = {}
    result: List[int] = []
    for i in array:
        if elements_amount.get(i) is None:
            elements_amount[i] = 1
        else:
            elements_amount[i] += 1
        if elements_amount[i] == n:
            result.append(i)

    elements_amount = None
    return result


# Заполняем массив случайными числами.
array: List[int] = []
for i in range(10):
    array.append(random.randint(1, 10))

print(array)
print(get_met_n(array, 0))
