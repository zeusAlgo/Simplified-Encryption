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

# def isPrime(x):  # primes
#     if x > 1:
#         for num in range(2, int(sqrt(x)) + 1):
#             if x % num == 0: return False
#         return True
#     return False


# primes = [val for val in range(1, 27) if isPrime(val)]
#
#
# def closestPrimes(cipher):
#     cipherArr = [int(string) for string in cipher.split()]
#     primeAr = []
#     for idx, val in enumerate(cipherArr):
#         sIdx, eIdx = 0, len(primes) - 1
#         while sIdx <= eIdx:
#             mIdx = (sIdx + eIdx) // 2
#             mVal = primes[mIdx]
#             # TODO: FINISH BSRXH
#             # if mVal == val:


# closestPrimes(encrypt('Regis'))
# encrypt('Regis')
# decrypt('23 9 12 12 7 5 20 6 15 15 4 21 14 5 5 4 20 15 7 5 20 3 8 1 9 14')


# Enter Your Prime

