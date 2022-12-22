import hashlib
# import embit
# from embit import bip39


diff = 3
leading_zeros = '0'*diff
for i in range(0, 100_000_000):
    hash_fmt = hashlib.sha256( str(i).encode() ).hexdigest()
    
    if leading_zeros == hash_fmt[0:diff]:
        print(hash_fmt)
        break
    
    # binary_fmt = "{0:08b}".format(int(hash_fmt, 16))
    # print(hash_fmt, str(binary_fmt))
