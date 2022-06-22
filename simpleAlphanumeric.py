from string import ascii_lowercase
from math import sqrt, inf


def encrypt(msg):  # Alphanumeric encryption scheme
    keys = [ch for ch in ascii_lowercase]
    encryptHashmap = dict(zip(keys, list(range(1, 27)))); encryptHashmap[' '] = ' '
    res = ' '.join(str(encryptHashmap[ch]) for ch in msg.lower())
    print(res); return res


def decrypt(cipher):  # Decryption
    vals = [ch for ch in ascii_lowercase]
    decryptHashmap = dict(zip(list(range(1, 27)), vals)); decryptHashmap[' '] = ' '
    res = ' '.join(decryptHashmap[int(ch)] for ch in cipher.split())
    print(res); return res

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

print('Please enter one of the following: \n 1 or 2')
print('1 = Encrypt')
print('2 = Decrypt')
res = input()

if res == '1':
    print('Please enter message to encrypt')
    encrypt(input())
elif res == '2':
    print('Please enter message to decrypt')
    decrypt(input())
else: 'Please try again'



