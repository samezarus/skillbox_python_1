print('Задача 2. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.

# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев
# и выводит на экран среднюю зарплату за год.

try:
    # Инициализируем
    months = 12
    salarys_summ = 0

    for month in range(1, months + 1):
        month_salary = int(input(f"Введите ЗП сотрудника за {month}-й месяц: "))
        salarys_summ += month_salary

    print()
    print(f"Средняя ЗП сотрудника за {months} месяцев равна: {int(salarys_summ / months)}")

except Exception as e:
    print(f"Что-то пошло не по плану: {e}")