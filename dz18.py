def get_unique_elements(lists):
    unique_elements = set()
    for sublist in lists:
        unique_elements.update(sublist)
    return unique_elements

if __name__ == '__main__':
    lists = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    unique_elements = get_unique_elements(lists)
    print(unique_elements)
