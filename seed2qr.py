import qrcode
import sys
from embit import bip39
# https://www.w3schools.in/python/classes-objects

# print(bip39.WORDLIST)


'''
word = 'addict'

print(bip39.WORDLIST.index(word))
# print(bip39.WORDLIST)
'''

'''
https://allprivatekeys.com/mnemonic-code-converter
https://github.com/meherett/python-hdwallet

111111111100011101011110001110000101001101011011111110000010101111100101110011010111110110111100111010110110011100000001010000010011000110011011110110110001000101011111111110000101000101011110111100100111100110010110010111111011100000101111110111111111111
15692029237316193423570985008487907853268984665640564039457554006913129639935
FFC75E38535BF82BE5CD7DBC75B380A098CDED88AFFC28AF793CCB2FDC17EFFF
FFC7 5E38 535B F82B E5CD 7DBC 75B3 80A0 98CD ED88 AFFC 28AF 793C CB2F DC17 EFFF
sewn forgery poorly armament surra pastor stoicism prog rupee panoply resigned worthy menses rehash acumen randy capping linkage reversal gilbert pygmy cozen snoopy pit
'''


seed_phrase = 'addict soldier tornado ketchup alien convince exercise machine quantum office obscure oxygen carpet carry cart case cash casino castle casual cat catalog catch category'.split()

data = ""
for word in seed_phrase:
    index = bip39.WORDLIST.index(word)
    data += str("%04d" % index)

hash = hex(int(data))

print(data)
print(hash)
# print(type(data))

qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make()
img = qr.make_image(fill_color="white", back_color="black").resize((370,370))
img.save("qr_seed.png")

'''
120,120
240,240
370,370 # default
480,480
700,700
'''

'''
qr = qrcode.QRCode( version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=5, border=3)
qr.add_data(data)
qr.make(fit=True)
qr.make_image(fill_color="black", back_color="white").resize((240,240)).convert('RGB').show()
'''
