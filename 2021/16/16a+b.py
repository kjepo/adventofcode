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

HEX = { '0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011', '4' : '0100', '5' : '0101',
        '6' : '0110', '7' : '0111', '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011', 
        'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111' }

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
    version, bits = bits[:3], bits[3:]
    versionsum += int(version, 2)
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
        if lengthbit == '0':
            length, bits = bits[:15], bits[15:]
            length = int(length, 2)
            subpackets, bits = bits[:length], bits[length:]
            values = []
            while len(subpackets):
                subpackets, value = eval(subpackets)
                values.append(value)
            return bits, apply(typeid, values)
        elif lengthbit == '1':
            nrsubpackets, bits = bits[:11], bits[11:]
            nrsubpackets = int(nrsubpackets, 2)
            values = []
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
