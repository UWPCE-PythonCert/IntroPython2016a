def char_map():
    import string
    return string.ascii_lowercase + string.ascii_lowercase

def add13(c):
    chars = char_map()
    counter = 0
    for l in chars:
        if l == c:
            position = counter
            break
        counter += 1
    return chars[counter + 13]

def sub13(c):
    chars = char_map()
    counter = 51
    for l in chars[::-1]:
        if l == c:
            position = counter
            break
        counter -= 1
    return chars[counter - 13]

def translate(s):
    text = ''
    for c in s:
        if c == ' ':
            text = text + ' '
        else:
            if c.isupper():
                text = text + sub13(c.lower()).upper()
            else:
                text = text + sub13(c.lower())
    return text

def encrypt(s):
    text = ''
    for c in s:
        if c == ' ':
            text = text + ' '
        else:
            if c.isupper():
                text = text + add13(c.lower()).upper()
            else:
                text = text + add13(c.lower())
    return text

if __name__ == '__main__':
    assert translate('Zntargvp sebz bhgfvqr arne pbeare') == 'Magnetic from outside near corner'
    assert encrypt('Magnetic from outside near corner') == 'Zntargvp sebz bhgfvqr arne pbeare'
