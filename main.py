from stats import get_word_count, get_character_count, sort_characters
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>' )
        sys.exit(1)
    
    path = sys.argv[1]
    text = get_book_text(path)
    wordcount = get_word_count(text)
    chars_dict = get_character_count(text)
    sorted_dict = sort_characters(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f'Found {wordcount} total words')
    print("--------- Character Count -------")
    
    for l,c in enumerate(sorted_dict):
        char = c['char']
        count = c['count']
        print(f"{char}: {count}")
    


main()