print('Задача 4. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
#
# Напишите программу,
# которая получает список оценок - N чисел - и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.

# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

try:
    # Инициализируем
    # троечники
    ratings_3 = 0
    # хорошисты
    ratings_4 = 0
    # отличники
    ratings_5 = 0
    # Кол-во учеников
    students = 10

    for student in range(1, students + 1):
        grade = 0

        # "пытаем" пользователя, что бы он вводил только правильные оценки
        while True:
            grade = int(input(f"Введите оценку (3/4/5) ученика № {student}: "))
            if grade > 2 and grade < 6:
                break

        if grade == 3:
            ratings_3 += 1
        elif grade == 4:
            ratings_4 += 1
        else:
            ratings_5 += 1

    print()
    if ratings_3 > ratings_4 and ratings_3 > ratings_5:
        print(f"Сегодня больше троечников, их {ratings_3}")
    elif ratings_4 > ratings_3 and ratings_4 > ratings_5:
        print(f"Сегодня больше хорошистов, их {ratings_4}")
    elif ratings_5 > ratings_3 and ratings_5 > ratings_4:
        print(f"Сегодня больше отличников, их {ratings_5}")

except Exception as e:
    print(f"Что-то пошло не по плану: {e}")