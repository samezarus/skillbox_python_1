print('Задача 6. Яйца')

# В рамках программы колонизации Марса
# компания «Спейс Инжиниринг» вывела особую породу черепах,
# которые, по задумке, должны размножаться, откладывая яйца в марсианском грунте.
# Откладывать яйца слишком близко к поверхности опасно из-за радиации,
# а слишком глубоко — из-за давления грунта и недостатка кислорода.
# Вообще, факторов очень много,
# но специалисты проделали большую работу и предположили,
# что уровень опасности для черепашьих яиц рассчитывается по формуле
# D = x**3 − 3x**2 − 12x + 10,
# где x — глубина кладки в метрах,
# а D — уровень опасности в условных единицах.
#
# Для тестирования гипотезы
# нужно взять пробу грунта на безопасной, согласно формуле, глубине.
#
# Напишите программу,
# находящую такое значение глубины "х", при котором уровень опасности как можно более близок к нулю.
# На вход программе подаётся максимально допустимое отклонение уровня опасности от нуля,
# а программа должна рассчитать приблизительное значение "х",
# удовлетворяющее этому отклонению.
#
# Известно, что глубина точно больше нуля и меньше четырёх метров.
#
# Обеспечьте контроль ввода.
#
# Пример:
# Введите максимально допустимый уровень опасности: 0.01
#
# Приблизительная глубина безопасной кладки: 0.732421875 м


def get_danger_level(depth: float):
    """
    Поиск уровня опасности в условных единицах

    :param depth: глубина грунта
    :return: уровень опасности
    """

    return depth**3 - 3 * depth**2 - 12 * depth + 10


def get_safety_depth(acceptable_level_: float, min_depth_: float, max_depth_: float) -> float:
    """
    Расчёт приблизительной глубины кладки яиц черепах

    :param acceptable_level_: допустимый уровень опасности
    :param min_depth_: верхний предел глубины (то что ближе к поверхности)
    :param max_depth_: нижний придел глубины (то что ближе к ядру)
    :return: приблизительная глубина безопасной кладки
    """

    # Ищем приблизительный центр (среднее арифметическое)
    result = (min_depth_ + max_depth_) / 2

    # Пока не найдём искомое
    while abs(get_danger_level(result)) >= acceptable_level_:
        # print("    ", result)

        # Сужаем пределы верха и низа (границы поиска)
        if abs(get_danger_level(max_depth_)) > abs(get_danger_level(min_depth_)):
            max_depth_ = result
        else:
            min_depth_ = result

        # Ищем приблизительный центр в сужающихся пределах (среднее арифметическое)
        result = (min_depth_ + max_depth_) / 2

    return result


try:
    # Инициализируем
    # Поверхность Марса
    min_depth = 0
    # Максимальня глубина
    max_depth = 4

    acceptable_level = float(input("Введите максимально допустимый уровень опасности: "))

    print()

    print(f"Приблизительная глубина безопасной кладки: {get_safety_depth(acceptable_level, min_depth, max_depth)}")

except Exception as e:
    print(f"Что-то пошло не по плану: {e}")
