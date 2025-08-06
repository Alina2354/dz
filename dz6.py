import os

def analyze_text_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        text = infile.read()

    num_chars = len(text)
    num_lines = text.count('\n') + 1
    num_vowels = 0
    num_consonants = 0
    num_digits = 0

    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    digits = "0123456789"

    for char in text:
        if char in vowels:
            num_vowels += 1
        elif char in consonants:
            num_consonants += 1
        elif char in digits:
            num_digits += 1

    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        outfile.write(f"Количество символов: {num_chars}\n")
        outfile.write(f"Количество строк: {num_lines}\n")
        outfile.write(f"Количество гласных букв: {num_vowels}\n")
        outfile.write(f"Количество согласных букв: {num_consonants}\n")
        outfile.write(f"Количество цифр: {num_digits}\n")

    print(f"Статистика успешно записана в файл: {output_file_path}")



if __name__ == '__main__':
    input_file = "file1.txt"
    output_file = "file2.txt"
    print(analyze_text_file(input_file, output_file))
