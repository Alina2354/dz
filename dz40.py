def split_names_ages(data):
    names = []
    ages = []
    for name, age in data:
        names.append(name)
        ages.append(age)
    return names, ages


if __name__ == '__main__':
    data = [('Alice', 30), ('Bob', 25), ('Charlie', 40)]
    names, ages = split_names_ages(data)
    print(f"Names: {names}")
    print(f"Ages: {ages}")


