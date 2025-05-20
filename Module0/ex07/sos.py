import sys
import string

MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',  ' ': '/'}


def translate_string(word):
    """Go through String and translate to Morse"""
    translation = ""
    for char in word:
        char = char.upper()
        translation += MORSE_CODE[char]
        translation += " "
    return translation


def main():
    """check User Input call translate Func"""
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return 1

    for char in sys.argv[1]:
        if (char not in string.ascii_letters and char != " "):
            print("AssertionError: the arguments are bad")
            return 1

    morse = translate_string(sys.argv[1])
    print(morse)


if __name__ == "__main__":
    main()
