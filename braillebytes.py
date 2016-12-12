#!/usr/bin/env python3

braille_base = 0x2800

def q(v, pos):
    if v & (1 << pos) != 0:
        return 1
    return 0

def braille(b):
    '''transform byte, so in braile bits will be ordered as:
    0 1 [0 3]
    2 3 [1 4] - first 4 from top are second hexa (and second first)
    4 5 [2 5]
    6 7 [6 7] - [] are actual braille order (6 extended)
    '''

    r = b & 0xE1 #0,5,6,7 unchanged
    r |= q(b, 2) << 1
    r |= q(b, 4) << 2
    r |= q(b, 1) << 3
    r |= q(b, 3) << 4
    return r


for b in range(0,256):
    bb = braille(b)
    print('%03d' % b, chr(braille_base + bb))
