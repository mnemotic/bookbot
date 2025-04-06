from stats import count_words, count_chars, sort_counts


def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        contents = file.read()
    return contents


def main() -> None:
    path = "books/frankenstein.txt"

    book_text = get_book_text(path)
    word_count = count_words(book_text)
    char_counts = sort_counts(count_chars(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for kvp in char_counts:
        char = kvp[0]
        count = kvp[1]
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
