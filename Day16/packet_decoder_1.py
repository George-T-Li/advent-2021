def main():
    with open("Day16\inputTest.txt") as f:
        packet = f.readline()
    packet = "38006F45291200" #test data
    print(f'{packet = }')
    parse(to_hex(packet))
    print(f'sum versions = {sum(versions)}')

def parse(packet):
    version = int(packet[:3], 2)
    type_ID = int(packet[3:6], 2)
    rest = packet[6:]

    if type_ID == 4:
        n = literal(rest)

    else:
        length_type_ID = int(rest[0])
        if length_type_ID: #case number of bits
            num_sp = int(rest[8:19], 2)
            subpackets = rest[19:19+num_sp]
            parse(subpackets)

        else: #case number of subpackets
            sp_length = int(rest[8:23], 2)
            subpackets = rest[23:]
            
def literal(b):
    b_val = ""
    i = 0

    while i < len(b):
        b_val += b[i+1:i+5]
        if b[i] == '0':
            break
        i += 5

    n = int(b_val, 2)
    return n

def to_hex(packet):
    p = packet.strip()
    return bin(int("1"+p, 16))[3:]

versions = []
if __name__ == "__main__":
    main()

    