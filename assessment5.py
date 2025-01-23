def word_frequency(text):
    text = text.lower()
    import string
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for word, count in word_count.items():
        print(f"{word}: {count}")
text = """This is a sample text. This text is just for testing the word frequency calculation. 
          Each word in this text should be counted."""
word_frequency(text)
