

def main():

    phrase_to_encode = "Michael"

    for char in phrase_to_encode:
        if char == ' ':
            continue

        phrase_to_encode.replace(char, (chr((ord(char) + 13))))
        print(char)

    print(phrase_to_encode)


if __name__ == '__main__':
    main()