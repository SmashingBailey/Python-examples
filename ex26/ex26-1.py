def break_words(stuff):
    """This function splits words"""
    split = stuff.split(' ')
    return split

def sort_words(words):
    """This function sorts words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints last word after popping off"""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(words):
    """Prints first and last words"""


sentence = "This is my sentence"

words = split_words(sentence)
