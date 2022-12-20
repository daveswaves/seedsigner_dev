import hashlib
# import embit
# from embit import bip39

for i in range(0, 100000000):
    hash_fmt = hashlib.sha256( str(i).encode() ).hexdigest()
    
    if '0000000' == hash_fmt[0:7]:
        print(hash_fmt)
        break
    
    # binary_fmt = "{0:08b}".format(int(hash_fmt, 16))
    # print(hash_fmt, str(binary_fmt))
