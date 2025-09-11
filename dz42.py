def merge_lists(*args):
    merged_list = []
    for lst in args:
        merged_list.extend(lst)
    return merged_list

if __name__ == '__main__':
    result1 = merge_lists([1, 2], ['a', 'b'], [3])
    print(f"Merged list 1: {result1}")

    result2 = merge_lists([1, 2, 3], [4, 5], [6, 7, 8])
    print(f"Merged list 2: {result2}")



