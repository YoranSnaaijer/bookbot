def main(path_to_file):
    file_contents = get_book_text(path_to_file)
    word_count = import_words(file_contents)
    print(f"{word_count} words found in the document")
    print(count_charachters(file_contents))

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents
    
def count_charachters(file_as_string):
    lowercase_string = file_as_string.lower()
    charachter_list = {}
    for charachter in lowercase_string:
        if charachter in charachter_list:
            charachter_list[charachter] += 1
        else:
            charachter_list[charachter] = 1
    return charachter_list

from stats import import_words
    
main("books/frankenstein.txt")
