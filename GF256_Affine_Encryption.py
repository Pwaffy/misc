ring = "010100110110010101100011010101000110111101110010"
rings = [int(ring[i:i+8], 2) for i in range(0, len(ring), 8)]
a = 0b00000111 
m = 0b100011011
def math(a, b, c):
    result = 0
    for i in range(7, -1, -1):
        if a >= 256:
            a ^= c
        if int(format(b, '08b')[i]):
            result ^= a
        a = a << 1

    return result

for byte in rings:
    thing = format(math(byte, a, m), '08b')
    print(f'{thing[:4]} {thing[4:]}')
