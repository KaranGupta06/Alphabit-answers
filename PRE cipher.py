word = input()
key = input()

real_key = key
ciphered_word = ''

while len(key) < len(word):
    key += real_key


for letter, subkey in zip(word, key):

    c_letter = ord(letter) + ord(subkey) - 97
    if c_letter > 122:
        c_letter -= 26
    ciphered_word += chr(c_letter)

print(ciphered_word)