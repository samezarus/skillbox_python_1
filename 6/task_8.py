print('Задача 8. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.

# Напишите программу,
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.

# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

# Подсказка: При желании найдите описание алгоритма бинарного поиска и попробуйте применить в этой задаче.
# Разбор подобного решения будет в следующем модуле.

""" Табуляцию поправил """

try:
    # Инициализируем
    # Пределы
    min_num = 1
    max_num = 100

    # Загаданное число мальчиком
    # prize = 51
    while True:
        prize = int(input(f"Какое число загадал мальчик (от {min_num} до {max_num}) ? "))
        if prize >= min_num and prize <= max_num:
            break

    # Вариант ПК (первым делом предполагаем, что искомое где-то в средине)
    pc_answer = max_num // 2

    # Попытки ПК
    pc_trys = 0

    while True:
        pc_trys += 1

        print()
        print(f"ПК: Твоё число равно, меньше или больше, чем число  {pc_answer} ?")

        if pc_answer > prize:
            print(f"Мальчик: 3 — меньше")
            max_num = pc_answer
        elif pc_answer < prize:
            print(f"Мальчик: 2 — больше")
            min_num = pc_answer
        else:
            print(f"Мальчик: 1 — равно")
            break

        pc_answer = min_num + ((max_num - min_num) // 2)

    print()
    print(f"ПК: Я угадал за {pc_trys} попыток")
except Exception as e:
    print(f"Что-то пошло не по плану: {e}")