def reverse_words(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)



if __name__ == '__main__':
    string1 = "The quick brown fox"
    reversed_string1 = reverse_words(string1)
    print(f"Original string: '{string1}'")
    print(f"Reversed string: '{reversed_string1}'")


