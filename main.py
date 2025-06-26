def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

def get_word_length(file_contents):
    return str(len(file_contents.split())) + " words found in the document"

def main():
    print(get_word_length(get_book_text('./books/frankenstein.txt')))

main()
