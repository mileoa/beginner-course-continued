#установка значения переменной количества первых целых чисел
n = int(input("Будет вычислена сумма N первых целых чисел начиная с 1. Введите N: "))
if n >= 1:
    #задаем переменную для хранения значения суммы
    sum = 0
    
    #суммируем все числа в диапазоне от 1 до n
    for i in range(n + 1):
        sum += i

    #выводим результат
    print("Сумма", n, "первых целых чисел начиная с 1 равна", sum)
else:
    print("Введённое число не может быть меньше единицы.")