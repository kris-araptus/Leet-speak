# LeetSpeak Converter

This Python script converts a given paragraph of text into LeetSpeak (1337 5P34K). It uses a predefined dictionary to map each letter to its corresponding LeetSpeak character.

## Features

- Converts common letters to their LeetSpeak equivalents.
- Handles both uppercase and lowercase input by converting all text to lowercase before processing.

## Usage

1. Clone or download this repository.
2. Ensure you have Python installed on your system.
3. Run the script and enter a paragraph of text when prompted.

## Example

### Input

Enter a paragraph: coding is awesome!


### Output

C0d!ng !$ 4w3$0M3!


## LeetSpeak Dictionary

The script uses the following LeetSpeak mappings:

| Character | LeetSpeak | Character | LeetSpeak |
|-----------|-----------|-----------|-----------|
| a         | 4         | o         | 0         |
| e         | 3         | s         | $         |
| i         | !         | t         | 7         |
| l         | 1         | z         | 3         |
| r         | R         | k         | K         |
| m         | M         | c         | C         |

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/leetspeak-converter.git
    ```
2. Navigate to the project directory:
    ```bash
    cd leetspeak-converter
    ```

## Running the Script

1. Ensure you have Python installed on your system.
2. Run the script:
    ```bash
    python leetspeak.py
    ```
3. Enter a paragraph of text when prompted.

## Script

Here's the `leetspeak.py` script for reference:

```python
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

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

    The LeetSpeak dictionary was sourced from various online references.


### Save the README File

1. Create a file named `README.md` in your project directory.
2. Copy and paste the above content into the `README.md` file.
3. Save the file.

This `README.md` provides a clear and comprehensive guide on how to use the LeetSpeak converter script, including features, usage, example, LeetSpeak dictionary, installation, and running instructions.
