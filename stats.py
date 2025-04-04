def count_words(string: str) -> int:
    words = string.split()
    return len(words)


def count_chars(string: str) -> dict[str, int]:
    char_counts = dict[str, int]()
    for char in string:
        char = char.lower()
        if not char in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    return char_counts
