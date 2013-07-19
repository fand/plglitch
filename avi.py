import sys
import struct

with open(sys.argv[1], 'rb') as f_in:
    binary = f_in.read()

idx1 = binary.index('idx1')
if idx1 != -1:
    movi  = binary.index('movi')

frames = []
len_idx1 = struct.unpack('<L', binary[idx1 + 4 : idx1 + 8])[0]
i = 8  # "idx1" + len_idx1(4bytes)
while i < len_idx1:
    # frame = (id, flag, offset, length)
    frames.append(struct.unpack('<4sLLL', binary[idx1+i: idx1+i+16]))
    i += 16

idx1_new , movi_new = binary[idx1:idx1+8], binary[movi:movi+4]

first = True
for f in frames:
    if f[0][:3] == '00d' and f[1] & 0x00000010 and not first:
        movi_new += f[0] + "\x00\x00\x00\x00"
    else:
        if first:
            first = False
        data = binary[movi + f[2] : movi + f[2] + f[3] + 8]
        if len(data) % 2 == 1:
            data += "\x00"
        movi_new += data        
        idx1_new += struct.pack('<4sLLL', f[0], f[1], f[2], f[3])

with open(sys.argv[2], 'wb') as f_out:
    f_out.write(binary[:movi] + movi_new + idx1_new)

