from stats import get_word_count, count_characters, sort_dictionary_list
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
    file_contents = get_book_text(filepath)
    word_count = get_word_count(file_contents)
    character_count = count_characters(file_contents)
    sorted_list = sort_dictionary_list(character_count)

    character_lines = "\n".join([f"{item['char']}: {item['num']}" for item in sorted_list])

    print(f'''============ BOOKBOT ============
    Analyzing book found at {filepath}...
    ----------- Word Count ----------
    Found {word_count} total words
    --------- Character Count -------
    {character_lines}
    ============= END ===============''')

main()
