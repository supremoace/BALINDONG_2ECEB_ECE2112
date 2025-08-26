def emotify(s):
    # Dictionary mapping words to emoticons
    emoticons = {
        "smile": ":)",
        "grin": ":D",
        "sad": ":(",
        "mad": ">:("
    }
    # Replace words in the sentence
    words = s.split()
    for i in range(len(words)):
        if words[i] in emoticons:
            words[i] = emoticons[words[i]]
    return ' '.join(words)

# Test cases
print(emotify("Make me smile"))
print(emotify("A big grin"))
print(emotify("I'm feeling sad"))
print(emotify("I am mad"))
