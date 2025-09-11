def is_prime(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(f"2 is prime: {is_prime(2)}")
    print(f"4 is prime: {is_prime(4)}")


