def sort_on(items):
    return items["num"]


def get_num_count(text):
    words = text.split()
    return len(words)


def count_chars(text):
    chars = {}
    for char in text:
        lowerChar = char.lower()
        if lowerChar in chars:
            chars[lowerChar] += 1
        else:
            chars[lowerChar] = 1
    return chars


def sort_list(char_count):
    items = []
    for char in char_count:
        items.append({"char": char, "num": char_count[char]})

    items.sort(reverse=True, key=sort_on)
    return items
