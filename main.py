def main(path_to_file):
    file_contents = get_book_text(path_to_file)
    word_count = import_words(file_contents)
    print(f"{word_count} words found in the document")

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents
    
from stats import import_words
    
main("books/frankenstein.txt")
