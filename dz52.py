import asyncio
import os

async def get_large_files(directory: str, min_size: int) -> list[str]:
    large_files = []

    if not os.path.isdir(directory):
        print(f"Директория не существует: {directory}")
        return []

    for entry in os.scandir(directory):
        if entry.is_file():
            try:
                file_size = entry.stat().st_size
                if file_size > min_size:
                    large_files.append(entry.path)
            except FileNotFoundError:
                print(f"Файл не найден: {entry.path}")

    return large_files


async def main():
    dir_path = "test_dir"
    os.makedirs(dir_path, exist_ok=True)

    file1_path = os.path.join(dir_path, "file1.txt")
    file2_path = os.path.join(dir_path, "file2.txt")
    file3_path = os.path.join(dir_path, "file3.txt")

    with open(file1_path, "w") as f:
        f.write("A" * 512)
    with open(file2_path, "w") as f:
        f.write("B" * 2048)
    with open(file3_path, "w") as f:
        f.write("C" * 1024)

    try:
        result = await get_large_files(dir_path, 1024)
        print(f"Крупные файлы: {result}")


    finally:
        for file_path in [file1_path, file2_path, file3_path]:
            try:
                os.remove(file_path)
            except FileNotFoundError:
                pass
        try:
            os.rmdir(dir_path)
        except OSError:
            print(f"Не удалось удалить директорию: {dir_path}")

if __name__ == "__main__":
    asyncio.run(main())
