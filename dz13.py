def count_characters_in_file(file_path):

    with open(file_path, 'r', encoding='utf-8') as infile:
        text = infile.read()
        character_count = len(text)
        return character_count



if __name__ == '__main__':
    file_path = "file1.txt"
    character_count = count_characters_in_file(file_path)
    if character_count > 0:
        print(f"Количество символов в файле: {character_count}")
    else:
        print("Файл пустой")
