import stats
import sys

if len(sys.argv)<2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()


def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    
    word_count = stats.count_words(book_text)
    characters = stats.count_characters(book_text)
    sorted_dicts = stats.sort_dict(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_dicts:
        if dict["char"].isalpha()==False:
            continue
        else:
            print(f"{dict['char']}: {dict['num']}")    

    print("============= END ===============")

main()