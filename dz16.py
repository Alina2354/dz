def count_word_frequency(text):

    word_counts = {}
    words = text.lower().split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

if __name__ == '__main__':
    text = "Привет привет мир Мир мир"
    word_frequency = count_word_frequency(text)
    print(word_frequency)
