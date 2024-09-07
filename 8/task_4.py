print('Задача 4. Отрезок')

# Напишите программу, которая считывает с клавиатуры три числа a, b и c, считает и выводит на
# консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.

try:
    # Инициализируем
    summ = 0
    found_count = 0

    # num_a = 1
    # num_b = 10
    # num_c = 3
    num_a = int(input("Введите начало отрезка: "))
    num_b = int(input("Введите конец отрезка: "))
    num_c = int(input("Введите число кратности: "))
    print()

    for item in range(num_a, num_b + 1):
        if item % num_c == 0:
            print(f"{item} = {num_c} * {item // num_c}")
            summ += item
            found_count += 1

    print()
    avg = int(summ/found_count)
    print(f"Среднее арифметическое всех чисел из отрезка [{num_a}; {num_b}], кратных числу {num_c} = {avg}")

except Exception as e:
    print(f"Что-то пошло не по плану: {e}")