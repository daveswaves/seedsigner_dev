'''
python3 ~/python_scripts/my_py/dice_roll.py
'''

import random
import hashlib
import embit # pip3 install embit
from typing import List
from embit import bip39

def generate_mnemonic_from_dice(roll_data: str) -> List[str]:
    entropy_bytes = hashlib.sha256(roll_data.encode()).digest()

    if len(roll_data) == 50:
        # 12-word mnemonic; only use 128bits / 16 bytes
        entropy_bytes = entropy_bytes[:16]

    # Return as a list
    return bip39.mnemonic_from_bytes(entropy_bytes).split()

def dice_rolls():
	dice_rolls = ""
	for i in range(0, 99):
		dice_rolls += str(random.randint(0, 5))
		# dice_rolls.append( str(random.randint(0, 5)) )
	
	mnemonic = generate_mnemonic_from_dice(dice_rolls)
	
	print(mnemonic)

dice_rolls()
