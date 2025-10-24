def analyze_range():
    print("--- Анализ чисел в диапазоне ---")
    while True:
        try:
            start = int(input("Введите первое число диапазона: "))
            end = int(input("Введите второе число диапазона: "))
            break
        except ValueError:
            print("Ошибка: Введите целые числа.")
    even_sum = 0
    even_count = 0
    odd_sum = 0
    odd_count = 0
    multiple_of_9_sum = 0
    multiple_of_9_count = 0

    for num in range(start, end + 1):
        if num % 2 == 0:
            even_sum += num
            even_count += 1
        else:
            odd_sum += num
            odd_count += 1

        if num % 9 == 0:
            multiple_of_9_sum += num
            multiple_of_9_count += 1

    print(f"\nДиапазон: от {start} до {end}")

    print("\nЧетные числа:")
    print(f"  Сумма: {even_sum}")
    if even_count > 0:
        print(f"  Количество: {even_count}")
        print(f"  Среднеарифметическое: {even_sum / even_count:.2f}")
    else:
        print("  Четных чисел нет в диапазоне.")

    print("\nНечетные числа:")
    print(f"  Сумма: {odd_sum}")
    if odd_count > 0:
        print(f"  Количество: {odd_count}")
        print(f"  Среднеарифметическое: {odd_sum / odd_count:.2f}")
    else:
        print("  Нечетных чисел нет в диапазоне.")

    print("\nЧисла, кратные 9:")
    print(f"  Сумма: {multiple_of_9_sum}")
    if multiple_of_9_count > 0:
        print(f"  Количество: {multiple_of_9_count}")
        print(f"  Среднеарифметическое: {multiple_of_9_sum / multiple_of_9_count:.2f}")
    else:
        print("  Чисел, кратных 9, нет в диапазоне.")

def draw_vertical_line():
    print("\n--- Вертикальная линия ---")
    while True:
        try:
            length = int(input("Введите длину линии: "))
            if length <= 0:
                print("Длина должна быть положительным числом.")
                continue
            break
        except ValueError:
            print("Ошибка: Введите целое число для длины.")

    symbol = input("Введите символ для заполнения линии: ")
    if not symbol:
        symbol = '*'
        print(f"Символ не введен, используем '{symbol}' по умолчанию.")
    elif len(symbol) > 1:
        symbol = symbol[0]
        print(f"Введено несколько символов, используем только первый: '{symbol}'")


    print("\nВаша вертикальная линия:")
    for _ in range(length):
        print(symbol)


def analyze_single_number():
    print("\n--- Анализ одного числа ---")
    while True:
        try:
            num = int(input("Введите число: "))
            break
        except ValueError:
            print("Ошибка: Введите целое число.")

    if num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")

    print("Good bye!")


def analyze_sequence_until_seven():
    print("\n--- Анализ последовательности чисел (до 7) ---")

    total_sum = 0
    max_num = None
    min_num = None
    count = 0

    print("Введите числа. Программа остановится, когда вы введете число 7.")

    while True:
        try:
            num = int(input("Введите число: "))

            if num == 7:
                break

            total_sum += num
            count += 1

            if max_num is None or num > max_num:
                max_num = num
            if min_num is None or num < min_num:
                min_num = num

        except ValueError:
            print("Ошибка: Введите целое число.")
            continue

    print("\nРезультаты анализа:")
    if count == 0:
        print("Числа (кроме 7) не были введены.")
    else:
        print(f"Сумма введенных чисел: {total_sum}")
        print(f"Максимальное число: {max_num}")
        print(f"Минимальное число: {min_num}")

    print("Good bye!")



if __name__ == "__main__":
    analyze_range()
    draw_vertical_line()
    analyze_single_number()
    analyze_sequence_until_seven()

