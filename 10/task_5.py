print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.


def num_sum(i: int) -> int:
    result = 0

    for item in str(i):
        result += int(item)

    return result


try:
    # Инициализируем
    max_sum: int = 0
    num: int = 0

    candidate_num: int = 0
    candidate_sum: int = 0

    # num_count = 1
    num_count: int = int(input("Введите количество чисел: "))
    print()

    for item in range(1, num_count + 1):
        candidate_num = int(input(f"Введите {item}-е чисел: "))
        candidate_sum  = num_sum(candidate_num)

        if candidate_sum > max_sum:
            max_sum = candidate_sum
            num = candidate_num

    print()
    print(f"Максимальное число {num}, сумма его чисел = {max_sum}")

except Exception as e:
    print(f"Что-то пошло не по плану: {e}")
