def replace_chars_in_file(input_file_path, output_file_path):

    with open(input_file_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        for line in lines:
            new_line = line.replace('*', '#TEMP#').replace('&', '*').replace('#TEMP#', '&')
            outfile.write(new_line)
    print(f"Файл {input_file_path} успешно обработан и записан в {output_file_path}")



if __name__ == '__main__':
    input_file = "file1.txt"
    output_file = "file2.txt"
    replace_chars_in_file(input_file, output_file)

