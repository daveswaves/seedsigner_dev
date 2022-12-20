import hashlib
import embit
from embit import bip39

'''
NOTES:
https://docs.python.org/3/library/hashlib.html
https://docs.python.org/3/library/binascii.html

2a65cc093ca1eed0826e716e74fd965e83c01ab7178b0cb61bf2379a6a877c1f
['clerk', 'common', 'across', 'junk', 'bus', 'hair', 'answer', 'soda', 'hover', 'pony', 'grain', 'rug', 'despair', 'ask', 'sword', 'vapor', 'arrow', 'radio', 'wish', 'hundred', 'pluck', 'dry', 'vacant', 'where']
'''

hash = '2a65cc093ca1eed0826e716e74fd965e83c01ab7178b0cb61bf2379a6a877c1f'

seed_phrase = bip39.mnemonic_from_bytes(hash.encode()).split()

print(seed_phrase)