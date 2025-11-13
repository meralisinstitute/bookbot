def count_words(text):
    return len(text.split())

def count_letters(text):
    
    text2 = list(text.lower())
    letter_counts = {}
    for char in text2:
        if char.isalpha():  # only count letters a-z
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts

def sort_on(items):
    return items["num"]