def import_words(text):
    words = len(text.split())
    return words

def count_charachters(file_as_string):
    lowercase_string = file_as_string.lower()
    charachter_list = {}
    for charachter in lowercase_string:
        if charachter in charachter_list:
            charachter_list[charachter] += 1
        else:
            charachter_list[charachter] = 1
    return charachter_list

def sort_list(charachter_list):
    def sort_on(dict):
        return dict["num"]
    letters = []
    for entry in charachter_list:
        dict = {"char": entry, "num": charachter_list[entry]}
        letters.append(dict)
    letters.sort(reverse=True, key=sort_on)
    return letters