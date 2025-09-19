import asyncio
import aiofiles
import os

async def count_lines_in_files(file_paths):
    results = {}

    async def count_lines(file_path):
        try:
            async with aiofiles.open(file_path, mode='r') as f:
                lines = await f.readlines()
                return len(lines)
        except FileNotFoundError:
            print(f"Файл не найден: {file_path}")
            return 0


    tasks = [count_lines(file_path) for file_path in file_paths]
    line_counts = await asyncio.gather(*tasks)

    for i, file_path in enumerate(file_paths):
        results[os.path.basename(file_path)] = line_counts[i]

    return results


async def main():

    file1_path = "file1.txt"
    file2_path = "file2.txt"
    file3_path = "file3.txt"

    async with aiofiles.open(file1_path, mode='w') as f:
        await f.write("Line 1\nLine 2\nLine 3")

    async with aiofiles.open(file2_path, mode='w') as f:
        await f.write("Line A\nLine B")

    async with aiofiles.open(file3_path, mode='w') as f:
        await f.write("Line X")

    file_paths = [file1_path, file2_path, file3_path, "nonexistent_file.txt"]

    try:
        results = await count_lines_in_files(file_paths)
        print(results)

    finally:

        for file_path in [file1_path, file2_path, file3_path]:
            try:
                os.remove(file_path)
            except FileNotFoundError:
                pass

if __name__ == "__main__":
    asyncio.run(main())
