# Get the paragraph from the user
paragraph = input("Enter a paragraph: ")

# Lists of letters and their corresponding characters
letters =    ['a', 'e', 'i', 'o', 's', 't' ,'l', 'z', 'r', 'k', 'm', 'c']
characters = ['4', '3', '!', '0', '$', '7', '1', '3', 'R', 'K', 'M', 'C']

# Create a translation dictionary from letters to characters
translation_dict = dict(zip(letters, characters))

# Translate the paragraph using the translation dictionary
translated_paragraph = ''.join(translation_dict.get(char, char) for char in paragraph)

print(translated_paragraph)
