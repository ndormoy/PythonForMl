import sys

sys.tracebacklimit = 0


def count_characters(str):
    """Counts the characters"""
    return len(str)


def count_uppercase(str):
    """Counts the uppercase characters"""
    return sum(1 for c in str if c.isupper())


def count_lowercase(str):
    """Counts the lowercase characters"""
    return sum(1 for c in str if c.islower())


def count_punctuation(str):
    """Counts the punctuation characters"""
    return sum(1 for c in str if c in ".,;:!?-\"'()")


def count_spaces(str):
    """Counts the spaces characters"""
    return sum(1 for c in str if c.isspace() or c == '\r' or c == '\n')


def count_digits(str):
    """Counts the digits characters"""
    return sum(1 for c in str if c.isdigit())


def read_input():
    """Reads input from the user and returns it as a string"""
    user_input = input("What is the text to count?\n")
    return user_input


def display_all(str):
    """Display all the counts"""
    print("The text contains", count_characters(str), "characters:")
    print("-", count_uppercase(str), "upper letters")
    print("-", count_lowercase(str), "lower letters")
    print("-", count_punctuation(str), "punctuation marks")
    print("-", count_spaces(str), "spaces")
    print("-", count_digits(str), "digits")


def main():
    # your tests and your error handling
    if (len(sys.argv) == 1):
        display_all(read_input())
    else:
        assert (not len(sys.argv) > 2), "more than one argument is provided"
        try:
            display_all(sys.argv[1])
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    """Main function"""
    main()
