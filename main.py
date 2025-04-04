from stats import count_words, count_chars


def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        contents = file.read()
    return contents


def main() -> None:
    book_text = get_book_text("books/frankenstein.txt")

    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")

    char_counts = count_chars(book_text)
    print(char_counts)


if __name__ == "__main__":
    main()
