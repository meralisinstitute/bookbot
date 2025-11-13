import sys
from stats import count_letters, count_words, sort_on

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, 'r') as f:
        text = f.read()

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    word_count = count_words(text)
    letter_count = count_letters(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    letter_list = [{"letter": k, "num": v} for k, v in letter_count.items()]
    letter_list.sort(reverse=True, key=sort_on)
    for item in letter_list:
        print(f"{item['letter']}: {item['num']}")
    print("============= END ===============")
if __name__ == "__main__":
    main()
