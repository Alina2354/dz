def count_word_occurrences(file_path, target_word):

    with open(file_path, 'r', encoding='utf-8') as infile:
        text = infile.read().lower()
        words = text.split()
        count = words.count(target_word.lower())
        return count


if __name__ == '__main__':
    file_path = "file1.txt"
    target_word = input("Введите слово для поиска: ")
    occurrences = count_word_occurrences(file_path, target_word)
    if occurrences > 0:
        print(f"Слово '{target_word}' встречается в файле {occurrences} раз(а).")
    else:
        print("Слово не найдено")
