import random

# Заполняем словарь случайными парами ключ - значение.
dictionary = {}
for i in range(100):
    # Генерируем случайный ключ.
    random_key = random.randint(-100, 100)
    while not isinstance(dictionary.get(random_key), type(None)):
        random_key = random.randint(-100, 100)
    
    # Генерируем случайное значение.
    random_value = []
    for k in range(random.randint(0, 100)):
        random_value.append(str(random.randint(0, 9)))
    
    # Записываем ключ-значение в словарь.
    dictionary[random_key] = "".join(random_value)
    assert len(dictionary) == i + 1

# Считываем все значения из словаря по ключу и печатаем их.
for key in dictionary:
    print(dictionary.get(key))

# Удаляем все пары.
for key in list(dictionary):
    dictionary.pop(key)
assert len(dictionary) == 0