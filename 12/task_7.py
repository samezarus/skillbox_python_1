from random import randint


print('Задача 7. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
#
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
#
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
#
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
#
# Камень бьёт ножницы,
# ножницы режут бумагу,
# бумага кроет камень.
#
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.


# Чтсло которое "загадал" ПК
pc_num = 5

# дикт с вариантами для игра "Камень, ножницы, бумага"
rps_items = {
    0: {
        "title": "Камень",
        "win": "бьёт",
        "loser": 1
    },
    1: {
        "title": "Ножницы",
        "win": "режут",
        "loser": 2
    },
    2: {
        "title": "Бумага",
        "win": "кроет",
        "loser": 0
    },
}

# кей (из rps_items) который "выбрал" ПК в игре "Камень, ножницы, бумага"
pc_rps_item = 1  # Ножницы


def rock_paper_scissors():
    # Здесь будет игра "Камень, ножницы, бумага"

    # Печатаем варианты предметов
    for key in rps_items:
        print(f'{key} - {rps_items[key].get("title")}')

    print()

    while True:
        user_rps_item = int(input("Выберите предмет: "))
        if user_rps_item != pc_rps_item:
            break
        else:
            print(f"{rps_items[user_rps_item].get("title")} на {rps_items[pc_rps_item].get("title")} - нмчья")
            print()

    print()
    print(f"И так, я загадал {rps_items[pc_rps_item].get("title")}, а вы выбрали {rps_items[user_rps_item].get("title")}")
    print()

    if rps_items[pc_rps_item].get("loser") == user_rps_item:
        print(f"Я победил, т.к. {rps_items[pc_rps_item].get("title")} {rps_items[pc_rps_item].get("win")} {rps_items[user_rps_item].get("title")}")
    else:
        print(f"Вы победили, т.к. {rps_items[user_rps_item].get("title")} {rps_items[user_rps_item].get("win")} {rps_items[pc_rps_item].get("title")}")


    print()
    print("Игра окончена !")


def guess_the_number():
    # Здесь будет игра "Угадай число"

    while True:
        user_num = int(input("Угадайте моё число: "))
        if (-1 < user_num < 10) and (user_num == pc_num):
            print()
            print(f"Вы угадали моё число, оно = {pc_num}")
            print("Игра окончена !")
            break


# Дикт структуры меню
menu_items = {
    1: {
        "title": "Камень, ножницы, бумага",
        "rules": "Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень",
        "link": rock_paper_scissors
    },
    2: {
        "title": "Угадай число",
        "rules": "Программа запрашивает у пользователя число до тех пор, пока он его не отгадает",
        "link": guess_the_number
    }
}


def main_menu():
    #Здесь главное меню игры
    print("Для вас доступны следующие игры:")
    print()

    for key in menu_items:
        print(f"{key} - {menu_items[key].get("title")}")

    while True:
        user_menu_item = int(input("Ваш выбор: "))
        if user_menu_item in menu_items.keys(): break

    print()
    print(f"Отлично, вы выбрали игру {menu_items[user_menu_item].get("title")}")
    print()

    print("Правила:")
    print(menu_items[user_menu_item].get("rules"))
    print()

    menu_items[user_menu_item].get("link")()

try:
    main_menu()

except Exception as e:
    print(f"Что-то пошло не по плану: {e}")
