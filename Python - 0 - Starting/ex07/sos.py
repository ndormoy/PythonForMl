import sys

sys.tracebacklimit = 0


def encode_morse_code(text):
    morse_code = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.", " ": "/",
    }
    encoded_text = []
    for char in text:
        char = char.upper()
        if char in morse_code:
            encoded_text.append(morse_code[char])
    return " ".join(encoded_text)


def main():
    """In main"""
    assert len(sys.argv) == 2, "You must provide exactly 1 argument"
    assert isinstance(sys.argv[1], str), "Argument must be a string"
    is_alphanumeric = all(
        char.isalnum() or char.isspace() for char in sys.argv[1])
    assert is_alphanumeric, "Argument must be alphanumeric or space"
    try:
        encoded_text = encode_morse_code(sys.argv[1])
        print(encoded_text)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    """Main function"""
    main()
