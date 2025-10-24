def print_numbers_1_to_10():
    print("--- Числа от 1 до 10 ---")
    number = 1
    while number <= 10:
        print(number)
        number += 1


def print_even_numbers_2_to_20():
    print("\n--- Четные числа от 2 до 20 ---")
    number = 2
    while number <= 20:
        print(number)
        number += 2

if __name__ == "__main__":
    print_numbers_1_to_10()
    print_even_numbers_2_to_20()
