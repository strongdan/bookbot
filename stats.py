def get_word_count(file_contents):
    return str(len(file_contents.split()))

def count_characters(file_contents):
    character_counts = []
    for character in file_contents:
        char = character.lower()
        if char.isalpha():
            for d in character_counts:
                if d['char'] == char:
                    d['num'] += 1
                    break
            else:
                character_counts.append({'char': char, 'num': 1})
    return character_counts

def sort_on(item):
    return item["num"]

# takes the dictionary of characters and their counts 
# and returns a sorted list of dictionaries
def sort_dictionary_list(character_dictionary_list):
    sorted_list = sorted(character_dictionary_list, reverse=True, key=sort_on)
    return sorted_list