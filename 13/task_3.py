print('Задача 3. Число наоборот 2')

# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225

def reverse_num_str(num: int) -> str:
    return str(num)[::-1]


def reverse_num_int(num: int) -> str:
    return int(reverse_num_str(num))


try:
    # Инициализируем
    user_num1 = int(input("Введите первое число: "))
    user_num2 = int(input("Введите второе число: "))
    print()

    reverse_num1 = reverse_num_int(user_num1)
    reverse_num2 = reverse_num_int(user_num2)
    reverse_summ = reverse_num1 + reverse_num2

    print(f"Первое число наоборот: {reverse_num1}")
    print(f"Второе число наоборот: {reverse_num2}")
    print()

    print(f"Сумма: {reverse_summ}")
    print(f"Сумма наоборот: {reverse_num_int(reverse_summ)}")

except Exception as e:
    print(f"Что-то пошло не по плану: {e}")