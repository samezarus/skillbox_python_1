print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

try:
    # Инициализируем
    count: int = int(input("Введите число: "))
    count_in_col: int = 0

    print()

    for row in range(1, count + 1):
        count_in_col += 1

        for col in range(count_in_col):
            print(row, end=' ')

        print()

except Exception as e:
    print(f"Что-то пошло не по плану: {e}")