import string

def alphabet_position(letter):
    return string.ascii_letters.index(letter.lower())

def rotate_character(char,rot):
    if char.isalpha():
        if char.islower():
            a = string.ascii_letters
        else:
            a = string.ascii_uppercase
        val = (alphabet_position(char)+ rot) %26
        return a[val]
    else:
        return char

def encrypt(text,rot):
    new_text = ""
    counter = 0
    if counter < len(text):
        for letter in text:
            new_text = new_text + rotate_character(letter,rot)
            counter += counter
    return new_text
