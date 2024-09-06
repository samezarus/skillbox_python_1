print('Задача 5. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль
# среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

# (среднее арифметическое можно посчитать поделив сумму подходящих чисел на их количество)

try:
    # Инициализируем
    multiplicity = 3
    found_summ = 0
    found_count = 0

    # point_a = 1
    # point_b = 14
    point_a = int(input(f"Введите a: "))
    point_b = int(input(f"Введите b: "))

    for item in range(point_a, point_b + 1):
        if item % multiplicity == 0:
            # print(item)
            found_summ += item
            found_count += 1

    print()
    print (f"Среднее арифметическое равно {int(found_summ/found_count)}")

except Exception as e:
    print(f"Что-то пошло не по плану: {e}")