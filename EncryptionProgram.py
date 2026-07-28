import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "

chars = list (chars)
key = chars.copy ()

random.shuffle(key)

#encrypt
plainText = input ("Enter a message to encrypt: ")
cipherText = ""

for letter in plainText:
    index = chars.index(letter)
    cipherText += key[index]

print(f"Origibal message: {plainText}")
print(f"Encrypted message: {cipherText}")

#decrypt
cipherText = input ("Enter a message to encrypt: ")
plainText = ""

for letter in cipherText:
    index = key.index(letter)
    plainText += chars[index]

print(f"Encrypted message: {cipherText}")
print(f"Origibal message: {plainText}")
