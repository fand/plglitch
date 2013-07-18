# flv.py
# 2013/05/18-
# @fand

import sys
import copy
import random
import binascii
import random

with open(sys.argv[1], "rb") as f:
    binary = f.read()

i = 13

codec = 0
removed_bytes = 0
removed_frame = 0
first = True

count = 0

while i < len(binary):
#while i < len(binary) - removed_bytes:
    if not (binary[i] in ["\x08", "\x09", "\x12"]):
        i += 4
        continue
    
    l = i + 11 + (ord(binary[i+1]) * 0x10000 +
                  ord(binary[i+2]) * 0x100 +
                  ord(binary[i+3]))

    # damage keyframes
    if binary[i] == "\x09" and ord(binary[i+11]) & 0xf0 == 0x10 and random.random() < 1.1:
        if first:
            first = False
            i = l+4
            continue

        # codec = ord(binary[i+11]) & 0x0f
        # s = ""
        # for j in range(i+13, l):
        #     if random.random() < 0.2:
        #         s += chr(random.randint(60, 230))
        #     else:
        #         s += binary[j]
        # binary = binary[:i+13] + s + binary[l:]
        binary = binary[:i] + binary[l+4:]
        removed_bytes += l+4 - i
        removed_frame += 1
        print(len(binary) - i)
        count += 1

        
    # damage audio
    # elif binary[i] == "\x08":
    #     if removed_frame != 0:
    #         binary = binary[:i] + binary[l+4:]
    #         removed_frame -= 1
    #         continue
            
        # s = ""
        # for j in range(i+15, l):
        #     if random.random() < 0.1:
        #         s += chr(random.randint(30, 230))
        #     else:
        #         s += binary[j]
        # binary = binary[:i+15] + s + binary[l:]
        # i = l+4

    else:
        i = l+4


print "#keyframe: ", count

with open(sys.argv[2], "wb") as f:
    f.write(binary)
    



