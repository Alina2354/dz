def compare_files(file1_path, file2_path):

    with open(file1_path, 'r', encoding='utf-8') as file1, \
         open(file2_path, 'r', encoding='utf-8') as file2:

        line_num = 1
        while True:
            line1 = file1.readline()
            line2 = file2.readline()

            if not line1 and not line2:
                print("Файлы идентичны.")
                return
            line1 = line1.rstrip('\n')
            line2 = line2.rstrip('\n')
            if line1 != line2:
                print(f"Строки не совпадают (строка {line_num}):")
                print(f"Файл 1: {line1}")
                print(f"Файл 2: {line2}")
                return

            line_num += 1


if __name__ == '__main__':
    file1_path = "file1.txt"
    file2_path = "file2.txt"

    print(compare_files(file1_path, file2_path))
