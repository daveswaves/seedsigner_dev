import os
import binascii
import hashlib
import embit # pip3 install embit
from embit import bip39
import unicodedata
import hashlib

'''
BIP39 basics: generating mnemonic and seed from entropy (bitcoin python) https://youtu.be/q_GgEHedfuI
https://allprivatekeys.com/mnemonic-code-converter
https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki
'''

bits = 256
'''
random_bin = os.urandom(bits//8) # random binary number
print(random_bin)
'''

hex = '68a79eaca2324873eacc50cb9c6eca8cc68ea5d936f98787c60c7ebc74e6ce7c'
random_bin = binascii.unhexlify(hex)
bytes = len(random_bin)
random_hex = binascii.hexlify(random_bin)

# 005b30a3ab171b8c3bed01ad5e340de09c0efab48ec02a82bac2081139d18663
hashed256 = hashlib.sha256(random_bin).hexdigest()
# print(hashed256)

# 011010001010011110011110101011...
bin_result256 = (
    bin(int(random_hex, 16))[2:].zfill(bytes*8)
    + bin(int(hashed256, 16))[2:].zfill(bits)[:bytes*8//32]
)
bin_result256_str = str(bin_result256)
# print(bin_result256_str)


# divide 256 bit binary into 11 bit segments
x = 11
binary_split_arr = [bin_result256_str[i: i + x] for i in range(0, len(bin_result256_str), x)]

# convert binary segments to decimal
index_list = []
for bin11 in binary_split_arr:
    index_list.append(int(bin11, 2))

# lookup indexes of decimal segments in BIP39 word list to get 24 words of seed phrase
word_list = []
for word_index in index_list:
    word_list.append(bip39.WORDLIST[word_index])

for index, bin11 in enumerate(binary_split_arr):
    index_lookup = str(index_list[index]).ljust(5, ' ')
    # print(f"{bin11} {index_lookup} {word_list[index]}")

print(index_list)
print(word_list)

seed_phrase = " ".join(word_list)

print(seed_phrase)

# Create BIP39 Seed
normalized_mnemonic = unicodedata.normalize("NFKD", seed_phrase)
password = ""
normalized_passphrase = unicodedata.normalize("NFKD", password)

passphrase = ("mnemonic" + normalized_passphrase).encode("utf-8")
mnemonic = normalized_mnemonic.encode("utf-8")

bin_seed = hashlib.pbkdf2_hmac("sha512", mnemonic, passphrase, 2048)

# 17e4b5661796eeff8904550f8572289317ece7c1cc1316469f8f4c986c1ffd7b9f4c3aeac3e1713ffc21fa33707d09d57a2ece358d72111ef7c7658e7b33f2d5
bip39seed = binascii.hexlify(bin_seed[:64])

print(bip39seed)

'''
Goto https://allprivatekeys.com/mnemonic-code-converter
and paste seed_phrase into 'BIP39 Mnemonic' field.
Page will calculate 'BIP39 Seed', 'BIP32 Extended Key'
and derived addresses.
TIP: Hover over to display QR code.

The above bip39seed value should be the same as the one the above webpage.
'''