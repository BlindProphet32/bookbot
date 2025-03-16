def get_word_count(contents):
    words = contents.split()
    return len(words)

def get_character_count(contents):
    chars = {}
    for c in contents:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["count"]

def sort_characters(chars):
    char_dict = []
    for l,c in chars.items():
        if l.isalpha():
            char_dict.append({"char": l, "count": c})
    char_dict.sort(reverse=True, key=sort_on)
    return char_dict