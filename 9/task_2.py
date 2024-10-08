print('Задача 2. Кривой мессенджер')

# Существует мессенджер, в котором иногда возникают неполадки при передаче сообщений: в них попадает лишний символ — звёздочка. Пользователям это надоело, поэтому они стали уходить в другие сервисы. Но один из них заинтересовался, на каких позициях обычно появляется звёздочка. Чтобы выяснить это, пользователю необходимо подготовить строки, в которых символ «*» встречается ровно один раз.

# Что нужно сделать:

# Напишите программу, которая определяет порядковый номер звёздочки в строке.

# Пример:

# Введите текст: «Пр*ивет как дела».
# Символ «*» стоит на позиции 3.

try:
    # Инициализируем
    char_pos: int = -1

    star_text: str = input("Введите текст: ")

    for index, char in enumerate(star_text):
        if char == '*':
            # print(f"Символ «*» стоит на позиции {index}")
            char_pos = index
            break

    print()
    if char_pos == -1:
        print(f"Символ «*» в строке не найден")
    else:
        print(f"Символ «*» стоит на позиции {char_pos}")

except Exception as e:
    print(f"Что-то пошло не по плану: {e}")