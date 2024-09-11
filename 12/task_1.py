print('Задача 1. Сумма чисел')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N
# и выводит сумму всех чисел от 1 до N включительно.
#
# Пример работы программы:
# Введите число: 5
#
# Я знаю, что сумма чисел от 1 до 5 равна 15


def summa_n(n: int) -> int:
    result: int = 0

    for i in range(1, n + 1):
        result += i

    return result


try:
    # Инициализируем
    user_num: int = int(input("Введите число: "))

    print()

    print(f"Я знаю, что сумма чисел от 1 до {user_num} равна {summa_n(user_num)}")

except Exception as e:
    print(f"Что-то пошло не по плану: {e}")