def remove_last_line(input_file_path, output_file_path):

    with open(input_file_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    lines = lines[:-1]
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        outfile.writelines(lines)
    print(f"Последняя строка удалена и результат записан в файл: {output_file_path}")



if __name__ == '__main__':
    input_file = "file1.txt"
    output_file = "file2.txt"
    print(remove_last_line(input_file, output_file))
