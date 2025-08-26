def alphabet_soup(word):
    # Create a list of characters from the string
    char_list = list(word)
    # Sort the list of characters
    char_list.sort()
    # Join the sorted list back into a string
    return ''.join(char_list)

# Test cases
print(alphabet_soup("hello"))
print(alphabet_soup("hacker"))