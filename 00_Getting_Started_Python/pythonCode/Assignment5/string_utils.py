def capitalize_words(text):
    words = text.split(" ")
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)


def reverse_string(text):
    return text[::-1]

def word_count(text):
    words = text.split(" ")
    return len(words)

