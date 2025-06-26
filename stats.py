def get_word_length(file_contents):
    return str(len(file_contents.split())) + " words found in the document"

def count_characters(file_contents):
    character_counts = {}
    for character in list(file_contents):
        if character.lower() in character_counts:
            character_counts[character.lower()] += 1
        else:
            character_counts[character.lower()] = 1
    return character_counts 
