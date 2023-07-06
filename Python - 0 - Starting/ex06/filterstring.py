import sys

sys.tracebacklimit = 0


def is_even(num):
    """Check if a number is even"""
    return num % 2 == 0


def manage_string(str, n):
    spliced = str.split()
    filtered = [x for x in spliced if len(x) > n]
    return filtered


def main():
    """In main"""
    assert (len(sys.argv) == 3), "You must have 2 arguments"
    assert ((type(sys.argv[1]) == str and not sys.argv[1].isdigit())
            and sys.argv[2].isdigit()), "argv[1] --> string, argv[2] --> int"
    try:
        print(manage_string(sys.argv[1], int(sys.argv[2])))
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    """Main function"""
    main()
