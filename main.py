from stats import get_word_length, count_characters

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

character_count = count_characters(get_book_text('./books/frankenstein.txt'))

def main():
    print(get_word_length(get_book_text('./books/frankenstein.txt')))
    print(character_count)

main()
