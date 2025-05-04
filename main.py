def main(path_to_file):
    file_contents = get_book_text(path_to_file)
    sorted_list = sort_list(count_charachters(file_contents))
    print(f"{import_words(file_contents)} words found in the document")
    for i in sorted_list:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents
    
from stats import import_words, count_charachters, sort_list
    
main("books/frankenstein.txt")
