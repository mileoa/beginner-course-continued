import random

# Функция возвращает массив элементов, которые встретились в переданном массиве >= n раз. 
def get_met_n(array, n):
    # Считаем сколько раз встречается элемент.
    dict = {}
    for i in array:
        if dict.get(i) is None:
            dict[i] = 1
            continue
        dict[i] += 1
    
    # Фильтруем элементы.
    for key, item in list(dict.items()):
        if item < n:
            dict.pop(key)
            
    return list(dict.keys())

# Заполняем массив случайными числами.
array = []
for i in range(100):
    array.append(random.randint(1, 10))

print(get_met_n(array, 1))