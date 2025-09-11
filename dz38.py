def multiply(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return float(a) * float(b)
    elif isinstance(a, str) and isinstance(b, int):
        return a * b
    elif isinstance(b, str) and isinstance(a, int):
        return b * a
    elif isinstance(a, str) and isinstance(b, str):
        raise ValueError("Cannot multiply two strings")
    else:
        raise TypeError("Operands must be numbers or a string and an integer")


if __name__ == '__main__':
    result1 = multiply(5, 3)
    print(f"5 * 3 = {result1}")
