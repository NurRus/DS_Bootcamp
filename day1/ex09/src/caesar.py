import sys

def check_cyrillic(text):
    return any('\u0400' <= char <= '\u04FF' for char in text)

def caesar_coding(text, shift, encode = True):
    result = []
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            if encode:
                new_char = chr((ord(char) - offset + shift) % 26 + offset)
            else:
                new_char = chr((ord(char) - offset - shift) % 26 + offset)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

def main():
    if len(sys.argv) != 4:
        raise ValueError("Invalid number of arguments")
    
    action, text, shift = sys.argv[1], sys.argv[2], int(sys.argv[3])

    if check_cyrillic(text):
        raise ValueError("The string contains Cyrillic characters")
    
    if action == 'encode':
        print(caesar_coding(text, shift, encode=True))
    elif action == 'decode':
        print(caesar_coding(text, shift, encode=False))
    else:
        raise ValueError("Invalid action. Use 'encode' or 'decode'.")
    
if __name__ == "__main__":
    main()
