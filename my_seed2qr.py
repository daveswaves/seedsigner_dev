import qrcode
import sys
from embit import bip39


# print(bip39.WORDLIST)


'''
word = 'addict'

print(bip39.WORDLIST.index(word))
# print(bip39.WORDLIST)
'''

seed_phrase = ['addict','soldier','tornado','ketchup','alien','convince','exercise','machine','quantum','office','obscure','oxygen','carpet','carry','cart','case','cash','casino','castle','casual','cat','catalog','catch','category']

data = ""
for word in seed_phrase:
    index = bip39.WORDLIST.index(word)
    data += str("%04d" % index)

# print(type(data))

qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make()
img = qr.make_image(fill_color="white", back_color="black")
img.save("qr_seed.png")


'''
qr = qrcode.QRCode( version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=5, border=3)
qr.add_data(data)
qr.make(fit=True)
qr.make_image(fill_color="black", back_color="white").resize((240,240)).convert('RGB').show()
'''
