import sys
import string

# String is no Function but a Modul from the pyhton standard library
# I guess the Subject is wrong try the String echo -n "" | wc  -> 170 chars

# Or with Copying the - gets Deleted because \n is expected but not used idk


def building():
    """
    This Function Prints the contens (elements)
    of a given String from the cli
    """
    argc = len(sys.argv)
    argv = sys.argv

    user_input = ""

    if (argc != 2):
        print("What is the text to count?")
        try:
            user_input = input() + "\n"
        except EOFError:
            print("\nEnd of input (Ctrl+D) detected.")
            return
    else:
        user_input = argv[1]

    all_chars = 0
    uppercase_num = 0
    lowercase_num = 0
    punctuation_count = 0
    digit_num = 0
    spaces_num = 0

    for char in user_input:
        all_chars += 1
        if char in string.punctuation:
            punctuation_count += 1
        if char in string.ascii_uppercase:
            uppercase_num += 1
        if char in string.ascii_lowercase:
            lowercase_num += 1
        if char in string.digits:
            digit_num += 1
        if char == " " or char == "\n":
            spaces_num += 1

    print(f"The text contains {all_chars} characters:")
    print(f"{uppercase_num} upper case letters")
    print(f"{lowercase_num} lower case letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{spaces_num} spaces")
    print(f"{digit_num} digits")


def main():
    building()


if __name__ == "__main__":
    main()
