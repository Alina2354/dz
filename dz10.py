def replace_word_in_file(file_path, old_word, new_word):

    with open(file_path, 'r', encoding='utf-8') as infile:
        text = infile.read()
    new_text = text.replace(old_word, new_word)
    with open(file_path, 'w', encoding='utf-8') as outfile:
        outfile.write(new_text)
    print(f"Слово '{old_word}' успешно заменено на '{new_word}' в файле {file_path}")


if __name__ == '__main__':
    file_path = "file1.txt"

    old_word = input("Введите слово, которое нужно заменить: ")
    new_word = input("Введите слово, на которое нужно заменить: ")
    replace_word_in_file(file_path, old_word, new_word)
