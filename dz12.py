def write_array_to_file(array, file_path):
        with open(file_path, 'w', encoding='utf-8') as outfile:
            for item in array:
                outfile.write(str(item) + '\n')

        print(f"Массив строк успешно записан в файл: {file_path}")



if __name__ == '__main__':

    string_array = [
        "Это первая строка",
        "Это вторая строка",
        "Это третья строка",
        "Это последняя строка"
    ]
    file_path = "file2.txt"

    write_array_to_file(string_array, file_path)
