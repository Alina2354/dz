def uniq_words(text):
    words = text.lower().split()
    unique_words = set(words)
    return unique_words

def count_words(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def top_words(word_counts):
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    top_3_words = sorted_word_counts[:3]
    return top_3_words

if __name__ == '__main__':
    text = "Привет как дела Привет все хорошо дела идут отлично Привет"
    unique_words = uniq_words(text)
    word_counts = count_words(text.lower().split())
    top_3 = top_words(word_counts)
    print(unique_words)
    print(word_counts)
    print(top_3)
