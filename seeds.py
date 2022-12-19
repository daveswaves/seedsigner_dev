'''
python3 ~/python_code/my_py/seeds.py
'''

import embit # pip3 install embit
from embit import bip39



seed_phrase = "acid aim bag bike box car core cry dad day dice dog else end era fan few fit fix fog jar key man two"
data_str = ""
data_spc = ""
for word in seed_phrase.split(" "):
    index = bip39.WORDLIST.index(word)
    data_str += "%04d" % index
    data_spc += "%04d " % index

print(seed_phrase)
print(data_spc)
print(data_str)
# print(bip39.WORDLIST[0])

for num, word in enumerate(bip39.WORDLIST):
   print(f"{num}: {word}")

# Enter data_str to the following QR Code Generator: https://www.the-qrcode-generator.com/