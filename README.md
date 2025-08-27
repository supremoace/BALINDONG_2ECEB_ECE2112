Programming Assignment 1

This repository contains my solutions for Programming Assignment 1.

Table of Contents
	•	Alphabet Soup Problem
	•	Emoticon Problem
	•	Unpacking List Problem

⸻

Programming Assignments

Alphabet Soup Problem

In this project, we are tasked to arrange the letters of a word in alphabetical order.
1.	I started with creating a function alphabet_soup(word) that will take a string input.
```python
def alphabet_soup(word):
    # Create a list of characters from the string
    char_list = list(word)
    # Sort the list of characters
    char_list.sort()
    # Join the sorted list back into a string
    return ''.join(char_list)
```
2.	I tested the function with different words:
```python
# Test cases
print(alphabet_soup("hello"))
print(alphabet_soup("hacker"))

 Output:

ehllo
acehkr
```

⸻

Emoticon Problem

In this project, we are tasked to change words into emoticons. Specifically: smile, grin, sad, and mad.
	1.	I started with creating a dictionary that maps words to their equivalent emoticons.

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

	2.	I tested the function with different sentences:

# Test cases
print(emotify("Make me smile"))
print(emotify("A big grin"))
print(emotify("I'm feeling sad"))
print(emotify("I am mad"))

✅ Output:

Make me :)
A big :D
I'm feeling :(
I am >:(


⸻

Unpacking List Problem

In this project, we are tasked to split a collection of numbers into three variables, namely first, middle, and last. The middle contains everything in between.
	1.	I started with a sample list.

listy = [1, 2, 3, 4, 5, 6]

	2.	Then, I unpacked the list into three parts.

# Unpacking
first, *middle, last = listy

	3.	Finally, I printed the results.

# Print results
print("first:", first, "middle:", middle, "last:", last)

✅ Output:

first: 1 middle: [2, 3, 4, 5] last: 6


⸻

Do you want me to also include links to your .ipynb file in GitHub (like in the example you gave), or just keep it clean with problems and solutions?
