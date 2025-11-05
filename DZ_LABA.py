import datetime


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число.")


def get_even_or_add_number(n: int):
    if n % 2 == 0:
        res = "Это число четное (even)."
    else:
        res = "Это число нечетное (odd)."
    return res


def task_1():
    print("\n--- Задача 1: Четное или нечетное ---")
    number = get_int_input("Введите число для проверки: ")
    result = get_even_or_add_number(number)
    print(f"Результат: {result}")


# --- Задача 2: Оценка по баллам ---
def task_2():
    print("\n--- Задача 2: Оценка по баллам ---")
    score = get_int_input("Введите количество баллов (0-100): ")

    if not (0 <= score <= 100):
        print("Ошибка: Баллы должны быть в диапазоне от 0 до 100.")
        return

    if score >= 90:
        grade = "Отлично"
    elif score >= 75:
        grade = "Хорошо"
    elif score >= 60:
        grade = "Удовлетворительно"
    else:
        grade = "Неудовлетворительно"

    print(f"Ваша оценка: {grade}")


# --- Задача 3: Определение времени суток ---
def task_3():
    print("\n--- Задача 3: Определение времени суток ---")
    hour = get_int_input("Введите время в часах (0-23): ")

    if not (0 <= hour <= 23):
        print("Ошибка: Время должно быть в диапазоне от 0 до 23.")
        return

    if 5 <= hour <= 11:
        time_of_day = "Утро"
    elif 12 <= hour <= 17:
        time_of_day = "День"
    elif 18 <= hour <= 21:
        time_of_day = "Вечер"
    else:  # 22, 23, 0, 1, 2, 3, 4
        time_of_day = "Ночь"

    print(f"Время суток: {time_of_day}")


# --- Задача 4: Класс по возрасту ---
def task_4():
    print("\n--- Задача 4: Класс по возрасту ---")
    age = get_int_input("Введите ваш возраст: ")

    if age < 0:
        print("Ошибка: Возраст не может быть отрицательным.")
        return

    if 0 <= age <= 12:
        category = "Дети"
    elif 13 <= age <= 17:
        category = "Подростки"
    else:  # 18 и старше
        category = "Взрослые"

    print(f"Вы попадаете в категорию: {category}")


# --- Задача 5: Сравнение двух чисел ---
def task_5():
    print("\n--- Задача 5: Сравнение двух чисел ---")
    num1 = get_int_input("Введите первое число: ")
    num2 = get_int_input("Введите второе число: ")

    if num1 > num2:
        print(f"Большее число: {num1}")
    elif num2 > num1:
        print(f"Большее число: {num2}")
    else:
        print("Числа равны.")


# --- Задача 6: Проверка на високосный год ---
def task_6():
    print("\n--- Задача 6: Проверка на високосный год ---")
    year = get_int_input("Введите год для проверки: ")
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    if is_leap:
        print(f"Год {year} является високосным.")
    else:
        print(f"Год {year} не является високосным.")


# --- Задача 7: Определение температуры ---
def task_7():
    print("\n--- Задача 7: Определение температуры ---")
    # Используем float, так как температура может быть дробной
    while True:
        try:
            temp = float(input("Введите температуру в градусах Цельсия: "))
            break
        except ValueError:
            print("Ошибка: Пожалуйста, введите числовое значение температуры.")

    if temp < 0:
        description = "Холодно"
    elif 0 <= temp <= 20:
        description = "Прохладно"
    elif 21 <= temp <= 30:
        description = "Тепло"
    else:  # temp > 30
        description = "Жарко"

    print(f"Описание погоды: {description}")


# --- Задача 8: Проверка на принадлежность к диапазону ---
def task_8():
    print("\n--- Задача 8: Проверка на принадлежность к диапазону ---")
    number = get_int_input("Введите число: ")

    if 10 <= number <= 20:
        print(f"Число {number} находится в диапазоне от 10 до 20 (включительно).")
    else:
        print(f"Число {number} НЕ находится в диапазоне от 10 до 20.")


# --- Задача 9: Определение знака зодиака ---
def task_9():
    print("\n--- Задача 9: Определение знака зодиака ---")
    day = get_int_input("Введите день рождения: ")
    month = get_int_input("Введите месяц рождения (1-12): ")

    if not (1 <= day <= 31 and 1 <= month <= 12):
        print("Ошибка: Некорректные дата или месяц.")
        return
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        sign = "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        sign = "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        sign = "Близнецы"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        sign = "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        sign = "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        sign = "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        sign = "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        sign = "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        sign = "Стрелец"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        sign = "Козерог"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        sign = "Водолей"
    else:
        sign = "Рыбы"

    print(f"Ваш знак зодиака: {sign}")


# --- Задача 10: Выбор напитка ---
def task_10():
    print("\n--- Задача 10: Выбор напитка ---")
    print("Выберите напиток:")
    print("1. Чай")
    print("2. Кофе")
    print("3. Сок")

    choice = get_int_input("Введите номер вашего выбора (1, 2 или 3): ")

    if choice == 1:
        drink = "Чай"
    elif choice == 2:
        drink = "Кофе"
    elif choice == 3:
        drink = "Сок"
    else:
        print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")
        return

    print(f"Вы выбрали: {drink}")


# --- Главная функция для запуска всех задач ---
def main():
    print("--- Запуск программы с 10 задачами на условные конструкции ---")

    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
    task_9()
    task_10()


if __name__ == "__main__":
    main()
