# Riddle 1
# URL:  http://www.pythonchallenge.com/pc/def/map.html

ciphertext = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. \
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.\
kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def decrypt(ciphertext):
    """Decrypt Caesar Cipher (key = 24) ciphertext, return plaintext as string."""
    plaintext = ""
    for char in ciphertext:
      if char in alphabet:
        plaintext += alphabet[alphabet.index(char) - 24]
      else:
        plaintext += char
    return plaintext

print(decrypt(ciphertext))

# Output:  i hope you didnt translate it by hand. thats what computers are for.
# doing it in by hand is inefficient and that's why this text is so long.
# using string.maketrans() is recommended. now apply on the url.

# Decrypt the last portion of the current URL
url_portion = "map"
print(decrypt(url_portion))

# Output:  ocr

# URL to Riddle 2:  http://www.pythonchallenge.com/pc/def/ocr.html
