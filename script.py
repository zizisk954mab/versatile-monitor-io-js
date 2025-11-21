#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Caesar Cipher Encryptor"""

def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    
    return result

if __name__ == "__main__":
    message = "Hello World"
    shift = 5
    
    encrypted = caesar_cipher(message, shift)
    decrypted = caesar_cipher(encrypted, -shift)
    
    print(f"Original: {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
