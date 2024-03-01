#!/usr/bin/env python3 
import random
import string

title_text = "Substitution Cipher"
subtitle_text = "TRY KEEP IT A SECRET"
author_text = "Created by Your Name/Team Name, 2024"
width = 80
height = 10

def center_text(text, banner_width):
    padding = (banner_width - len(text)) // 2
    return " " * padding + text + " " * padding

lines = [
    "#" * width,
    "#" + center_text(title_text, width - 2) + "#",
    "#" * width,
    "#" + center_text(subtitle_text, width - 2) + "#",
    "#" * width,
]

# DISPLAYING BANNER
print("\n")
for line in lines:
    print(line)
print("\n")

# CREATING CHARACTERS
all_characters = list(" " + string.ascii_letters  + string.digits + string.punctuation)
key = all_characters.copy()
random.shuffle(key)


#ENCRYPTING TEXT
print(" [========================================| ENCRYPTING |========================================]\n")
plain_text = input("[+] Enter Text To Encrypt: ")
cipher_text = ""

for letter in plain_text:
    letter_index = all_characters.index(letter)
    cipher_text += key[letter_index]
    
print("\n[-] Cipher Text : ", cipher_text, "\n")

#DECRYPTING TEXT
print(" [========================================| DECRYPTING |========================================]\n")
cipher_text = input("[+] Enter Text To Decrypt: ")
plain_text = ""

for letter in cipher_text:
    letter_index = key.index(letter)
    plain_text += all_characters[letter_index]
    
print("\n[-] Plain Text : ", plain_text, "\n")
