print('Задача 7. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29



"""
Это просто жесть, убил весь вечер, но зато моя пирамида маштабируется в любом количестве уровней

"""


def get_max_num(levels_: int) -> int:
    """
    Ищем максимальное число в пирамиде

    :param levels_: Кол-во уровней
    :return: максимальное число
    """

    result: int = 1

    bricks_on_level = 1

    for i in range(levels_):

        for j in range(bricks_on_level):
            result += 2

        bricks_on_level += 1

    return result - 2


def num_for_print(max_num_: int, i: int) -> str:
    """
    Готовим число для вывода. Сравниваем с длиной самого большого и добиваем
    пробелами если надо ...

    :param max_num_: Максимальное число в прирамиде
    :param i: Число для добивания пробелами
    :return: Готовое к выводу число
    """

    result: str = ""

    max_num_str = str(max_num_)
    i_str = str(i)

    if len(i_str) < len(max_num_str):
        result = i_str + ' ' * (len(max_num_str) - len(i_str))
    else:
        result = i_str

    return result


try:
    # Инициализируем
    # Кол-во цифр (кирпичей) на уровне
    bricks: int = 1

    # Значение цифры/Кирпич
    num = 1

    # Кол-во уровней пирамиды
    # levels: int = 30
    levels: int = int(input("Введите количество уровней пирамиды: "))

    # Максимальное число в пирамиде для вычисления его строковой длины
    max_num = get_max_num(levels)

    # Кол-во отступов слева
    indents: int = levels -1

    # Размер отступа слева
    indent_len = ' ' * (len(str(max_num)) + 1)

    # Расстояние между цифрами (кирпичами)
    brick_divider = indent_len + ' '

    # Обход уровней пирамиды
    for level in range(levels):
        # Ставим отступы слева
        for indent in range(indents):
            print(indent_len, end='')

        # Ставим кирпичи (#)
        for brick in range(bricks):
            print(num_for_print(max_num, num), end=brick_divider)
            num += 2

        # После прохода каждого уровня добавляем +2 кирпича относительно предыдущего
        bricks += 1

        # После прохода каждого уровня уменьшаем отступ слева
        indents -= 1

        print()

except Exception as e:
    print(f"Что-то пошло не по плану: {e}")