def group_anagrams(words):
    anagram_groups = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    result = list(anagram_groups.values())
    return result


if __name__ == '__main__':
    words = ["listen", "silent", "hello", "world", "dog", "god"]
    anagram_groups = group_anagrams(words)
    print(anagram_groups)
