alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def encrypt(text, shift):
    text = [letter for letter in text]

    for i in range(0, len(text)):
        encryptedCharacterIndex = alphabet.index(text[i]) + shift
        if encryptedCharacterIndex >= 26:
            encryptedCharacterIndex = encryptedCharacterIndex - 26
        
        text[i] = alphabet[encryptedCharacterIndex]
    
    return "".join(text)


def decrypt(text, shift):
    text = [letter for letter in text]

    for i in range(0, len(text)):
        decryptedCharacterIndex = alphabet.index(text[i]) - shift
        if decryptedCharacterIndex < 0:
            decryptedCharacterIndex = decryptedCharacterIndex + 26
        
        text[i] = alphabet[decryptedCharacterIndex]
    
    return "".join(text)


print(encrypt("rishi", 3))
print(decrypt(encrypt("rishi", 3), 3))