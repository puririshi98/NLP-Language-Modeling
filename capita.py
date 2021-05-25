

from segtok import tokenizer

def preprocess_capitalization(text):
    words = tokenizer.word_tokenizer(text)
    final_words = []
    for word in words:
        if not word.isalpha():
            final_words.append(word.lower())
        else:
            if word.islower():
                pass
            elif word.isupper():
                final_words.append("⇧")
            elif word[0].isupper() and word[1:].islower():
                final_words.append("↑")
            else:
                final_words.append("↑")

            final_words.append(word.lower())
    return " ".join(final_words)
            
def unprocess_capitalization(text):
    words = text.split(" ")
    final_words = []
    all_caps = False; capitalized = False
    for w in words:
        if w == "⇧": all_caps = True
        elif w == "↑": capitalized = True
        else:
            final_word = w
            if all_caps: final_word = final_word.upper()
            elif capitalized:
                if len(final_word) <= 1: final_word = final_word.upper()
                else: final_word = final_word[0].upper()+final_word[1:]
            final_words.append(final_word)
            all_caps = False; capitalized = False

    return " ".join(final_words)