def sort(array):
    xchange = True

    while xchange:
        xchange = False # предполагаем, что массив уже отсортирован

        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                # нашли элементы,
                # неупорядоченные по возрастанию:
                # меняем их местами:
                array[i], array[i+1] = array[i+1], array[i]

                # цикл проверки массива надо продожить снова:
                xchange = True
    return array
