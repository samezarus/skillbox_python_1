print('Задача 3. Апгрейд калькулятора')

# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные арифметические действия.
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом:
# вывести сумму его цифр,
# максимальную или минимальную цифру.

#Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.


actions = {
    0: "Вывести сумму цифр числа",
    1: "Вывести максимальную цифру числа",
    2: "Вывести минимальную цифру числа"
}


def print_actions():
    print()
    print("Поддерживаемые команды:")

    for key in actions:
        print(f"{key} - {actions[key]}")


def summa_num(num: int) -> int:
    result: int = 0

    num_copy = num * 10

    while num_copy // 10 != 0:
        num_copy //= 10
        result += num_copy % 10

    return result


def num_min(num: int) -> int:
    result: int = 9

    num_copy = num * 10

    while num_copy // 10 != 0:
        num_copy //= 10

        num_item = num_copy % 10

        if num_item < result:
            result = num_item

    return result


def num_max(num: int) -> int:
    result: int = 0

    num_copy = num * 10

    while num_copy // 10 != 0:
        num_copy //= 10

        num_item = num_copy % 10

        if num_item > result:
            result = num_item

    return result


def transformer():
    user_num = int(input("Введите чисо для обработки: "))

    print_actions()

    # Проверяем на ввод допустимых команд
    while True:
        user_action = int(input("Введите команду: "))
        if user_action in actions.keys():
            break

    print()

    title: str = f"{actions[user_action]} ="

    if user_action == 0:
        print(f"{title} {summa_num(user_num)}")
    elif user_action == 1:
        print(f"{title} {num_max(user_num)}")
    elif user_action == 2:
        print(f"{title} {num_min(user_num)}")
    else:
        pass


try:
    transformer()

except Exception as e:
    print(f"Что-то пошло не по плану: {e}")