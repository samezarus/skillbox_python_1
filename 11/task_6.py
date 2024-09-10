print('Задача 6. Ход конём')


# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.



"""
Референсы

|  0:0  |  1:0  |  2:0  |  3:0  |  4:0  |  5:0  |  6:0  |  7:0  |
|  0:1  | *1:1* |  2:1  | *3:1* |  4:1  |  5:1  |  6:1  |  7:1  |
|  0:2  |  1:2  |  2:2  |  3:2  |  4:2  |  5:2  |  6:2  |  7:2  |
|  0:3  |  1:3  | [2:3] |  3:3  |  4:3  |  5:3  |  6:3  |  7:3  |
|  0:4  |  1:4  |  2:4  |  3:4  |  4:4  |  5:4  |  6:4  |  7:4  |
|  0:5  | *1:5* |  2:5  | *3:5* |  4:5  |  5:5  |  6:5  |  7:5  |
|  0:6  |  1:6  |  2:6  |  3:6  |  4:6  |  5:6  |  6:6  |  7:6  |
|  0:7  |  1:7  |  2:7  |  3:7  |  4:7  |  5:7  |  6:7  |  7:7  |

Эмпирическим путём по клеткам вверху выяснил что после вычитания по модулю из новой клетки текущей 2 и 1 что соответствует 
траектории хождения коня буквой "Г", что бы не сравнивать что-то вроде
 
if (x - x_new == 1 and y - y_new = 2) or (x - x_new == 2 and y - y_new = 1):
    pass
    
просто их складываю и получаю 3

"""

def in_range(i: float) -> bool:
    """
    Проверка вводимого числа на меньше 1 и больше ноля

    :param i: Проверяемое число
    :return: Результат
    """

    # принадлежит
    if (i < 1) and (i < 8):
        return True
    # не принадлежит
    else:
        return False


try:
    print("Значения X и Y должны быть дробными и больше ноля но меньше единицы")
    print()

    # Инициализируем
    while True:
        horse_x: float = float(input("Введите X местоположение коня: "))
        if in_range(horse_x):
            break

    while True:
        horse_y: float = float(input("Введите Y местоположение коня: "))
        if in_range(horse_y):
            break

    while True:
        new_horse_x: float = float(input("Введите X местоположение точки на доске: "))
        if in_range(new_horse_x):
            break

    while True:
        new_horse_y: float = float(input("Введите Y местоположение точки на доске: "))
        if in_range(new_horse_y):
            break

    # horse_x_int: int = 0
    # horse_y_int: int = 1
    # new_horse_x_int: int = 2
    # new_horse_y_int: int = 0

    horse_x_int: int = int(horse_x * 10)
    horse_y_int: int = int(horse_y * 10)
    new_horse_x_int: int = int(new_horse_x * 10)
    new_horse_y_int: int = int(new_horse_y * 10)

    print()
    print(f"Конь в клетке [ {horse_x_int}:{horse_y_int} ]. Точка в клетке [ {new_horse_x_int}:{new_horse_y_int} ]")
    print()

    # Магическое число, которое говорит может ли конь пройти буквой "Г" в указанную точку
    super_num: int = abs(new_horse_x_int - horse_x_int) + abs(new_horse_y_int - horse_y_int)

    if super_num == 3:
        print(f"Да, конь может ходить в эту точку")
    else:
        print(f"Нет, конь не может ходить в эту точку")

except Exception as e:
    print(f"Что-то пошло не по плану: {e}")