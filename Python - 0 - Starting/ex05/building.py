import sys

sys.tracebacklimit=0

def count_characters(str):
    """Counts the characters"""
    return len(str)

def count_uppercase(str):
    """Counts the uppercase characters"""
    count = 0
    for char in str:
        if char.isupper():
            count += 1
    return count

def count_lowercase(str):
    """Counts the lowercase characters"""
    count = 0
    for char in str:
        if char.islower():
            count += 1
    return count

def count_punctuation(str):
    """Counts the punctuation characters"""
    count = 0
    for char in str:
        if char in ".,;:!?":
            count += 1
    return count

def count_spaces(str):
    """Counts the spaces characters"""
    count = 0
    for char in str:
        if char.isspace():
            count += 1
    return count

def count_digits(str):
    """Counts the digits characters"""
    count = 0
    for char in str:
        if char.isdigit():
            count += 1
    return count

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
        print("No argument")
    else:
        assert(not len(sys.argv) > 2), "more than one argument is provided"
        try:
            display_all(sys.argv[1])
        except AssertionError as e:
            print(e)

if __name__ == "__main__":
    """Main function"""
    main()