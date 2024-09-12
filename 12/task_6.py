print('Задача 6. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел


def get_gcd(num1: int, num2: int) -> int:
    result = 1

    min_num = num1 if num1 < num2 else num2

    for d in range(1, min_num):
        if num1 % d == 0 and num2 % d == 0:
            if d > result: result = d

    return result


try:
    # Инициализируем
    user_num1 = int(input("Введите первое число: "))
    user_num2 = int(input("Введите второе число: "))

    print()

    print(f"Наибольший общий делитель = {get_gcd(user_num1, user_num2)}")

except Exception as e:
    print(f"Что-то пошло не по плану: {e}")
