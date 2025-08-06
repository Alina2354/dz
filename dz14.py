def count_lines_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as infile:
        line_count = 0
        for line in infile:
            line_count += 1
        return line_count


if __name__ == '__main__':
    file_path = "input.txt"
    line_count = count_lines_in_file(file_path)
    if line_count > 0:
        print(f"Количество строк в файле: {line_count}")
    else:
        print("Файл пустой")
