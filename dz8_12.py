def calculate_expression():
    print("Введите арифметическое выражение (например, 23+12).")
    print("Поддерживаемые операции: +, -, *, /")

    while True:
        expression = input("Ваше выражение: ").strip()

        if not expression:
            print("Выражение не может быть пустым. Попробуйте еще раз.")
            continue

        import re
        match = re.match(r'(\d+)([-+*/])(\d+)', expression)

        if not match:
            print("Некорректный формат выражения. Используйте формат 'число_операция_число' (например, 23+12).")
            continue

        try:
            num1_str, operator, num2_str = match.groups()
            num1 = int(num1_str)
            num2 = int(num2_str)

            result = None
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Ошибка: Деление на ноль невозможно.")
                    continue
                result = num1 / num2
            else:
                print("Неизвестная операция.")
                continue

            print(f"Результат: {expression} = {result}")
            break
        except ValueError:
            print("Ошибка: Неверный формат чисел. Убедитесь, что вы вводите целые числа.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")


import random


def analyze_random_list(size=10, min_val=-100, max_val=100):
    print("\n--- Анализ списка случайных чисел ---")
    numbers = [random.randint(min_val, max_val) for _ in range(size)]
    print(f"Сгенерированный список: {numbers}")

    if not numbers:
        print("Список пуст, анализ невозможен.")
        return

    min_element = numbers[0]
    max_element = numbers[0]
    negative_count = 0
    positive_count = 0
    zero_count = 0

    for num in numbers:
        if num < min_element:
            min_element = num
        if num > max_element:
            max_element = num

        if num < 0:
            negative_count += 1
        elif num > 0:
            positive_count += 1
        else:  # num == 0
            zero_count += 1

    print(f"Минимальный элемент: {min_element}")
    print(f"Максимальный элемент: {max_element}")
    print(f"Количество отрицательных элементов: {negative_count}")
    print(f"Количество положительных элементов: {positive_count}")
    print(f"Количество нулей: {zero_count}")

