def get_book_text(filepath):
    # print(f"Filepath: {filepath}")
    with open(filepath) as f:
        return f.read()


def get_word_count(text):
    text_split = text.split()
    return len(text_split)


def main():
    word_count = get_word_count(
        get_book_text(
            "/home/Dami3n/workspace/github.com/bootdotdev/bookbot/books/frankenstein.txt"
        )
    )
    print(f"Found {word_count} total words")


main()
