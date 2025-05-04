def main(path_to_file):
    file_contents = get_book_text(path_to_file)
    sorted_list = sort_list(count_charachters(file_contents))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {import_words(file_contents)} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents
    
from stats import import_words, count_charachters, sort_list
import sys

try:
    file_location = sys.argv[1]
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])
