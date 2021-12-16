#!/usr/bin/env python3

import sys
import math

# packet    -> version literal | version operator
# version   -> bit bit bit
# typeid    -> bit bit bit
# bit       -> 0 | 1
# body      -> literal | operator
# literal   -> 1 0 0 digits
# digits    -> 1 number digits | 0 number
# operator  -> op-prefix op-rest
# op-prefix -> 0 0 0 | 0 0 1 | 0 1 0 | 0 1 1 | 1 0 1 | 1 1 0 | 1 1 1
# op-rest   -> 0 length15 ( packet ... )*
# op-rest   -> 1 length11 ( packet ... )*
# length15  -> bit bit .. bit   (15 bits)
# length11  -> bit bit .. bit   (11 bits)

HEX = { }
for n in range(16):
    HEX[hex(n)[2].upper()] = f'0b{n:04b}'[2:]

def apply(op, values):
    if op == 0:
        return sum(values)
    if op == 1:
        return math.prod(values)
    if op == 2:
        return min(values)
    if op == 3:
        return max(values)
    if op == 5:
        return 1 if values[0] > values[1] else 0
    if op == 6:
        return 1 if values[0] < values[1] else 0
    if op == 7:
        return 1 if values[0] == values[1] else 0
    print("Illegal operation: op =", op)
    exit(0)

# recursive descent parser for packet - returns a numeric value
def eval(bits):                 
    global versionsum
    version, bits = int(bits[:3], 2), bits[3:]
    versionsum += version
    typeid, bits = int(bits[:3], 2), bits[3:]
    if typeid == 4:         # literal value
        digits = []
        while bits[0] == '1':
            bits = bits[1:]
            digit, bits = bits[:4], bits[4:]
            digits.append(digit)
        bits = bits[1:]
        digit, bits = bits[:4], bits[4:]
        digits.append(digit)        
        return bits, int(''.join(digits), 2)
    else:                       # operator
        lengthbit, bits = bits[0], bits[1:]
        values = []
        if lengthbit == '0':
            length, bits = int(bits[:15], 2), bits[15:]
            subpackets, bits = bits[:length], bits[length:]
            while subpackets:
                subpackets, value = eval(subpackets)
                values.append(value)
            return bits, apply(typeid, values)
        elif lengthbit == '1':
            nrsubpackets, bits = int(bits[:11], 2), bits[11:]
            for _ in range(nrsubpackets):
                bits, value = eval(bits)
                values.append(value)
            return bits, apply(typeid, values)
            
if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        versionsum = 0
        for line in lines:
            bits = ''.join([ HEX[b] for b in line.strip()])
            (_, value) = eval(bits)
            print("versionsum = ", versionsum)
            print("-->", value)
    
