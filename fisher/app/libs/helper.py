def is_isbn_or_keyword(word='word'):
    if word.isdigit():
        word = 'isbn'
    else:
        word = 'word'
    return word
