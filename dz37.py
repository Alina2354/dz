def divide(numerator, denominator):
    if not isinstance(numerator, (int, float)):
        raise TypeError("Numerator must be a number (int or float)")
    if not isinstance(denominator, (int, float)):
        raise TypeError("Denominator must be a number (int or float)")
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return numerator / denominator

if __name__ == '__main__':

    result1 = divide(10, 2)
    print(f"10 / 2 = {result1}")

