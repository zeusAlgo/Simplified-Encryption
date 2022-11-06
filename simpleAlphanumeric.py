from string import ascii_lowercase

def encrypt(plainText):  # Alphanumeric encryption scheme
    encryptHashmap = {char: idx for idx, char in enumerate(ascii_lowercase, 1)}
    encryptHashmap[' '] = ' '
    res = ' '.join(str(encryptHashmap[char]) for char in plainText.lower())
    print(res); return res


def decrypt(cipherText):  # Decryption
    decryptHashmap = {idx: char for idx, char in enumerate(ascii_lowercase, 1)}
    decryptHashmap[' '] = ' '
    res = ' '.join(decryptHashmap[int(char)] for char in cipherText.split())
    print(res); return res


print('Please enter one of the following: \n 1 or 2 \n')
print('1 = Encrypt \n2 = Decrypt')
res1 = input().strip()

if res1 == '1':
    print('Please enter plain text to encrypt')
    encrypt(input())
elif res1 == '2':
    print('Please enter cipher text to decrypt')
    decrypt(str(input()))
else: 'Please try again'
