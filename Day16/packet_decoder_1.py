def main():
    with open("Day16\input.txt") as f:
        packet = f.readline()
    #packet = "620080001611562C8802118E34" #test data
    parse(to_hex(packet))
    print(f'sum versions = {sum(versions)}')

def parse(packet):
    print(f'{packet = }')
    if packet == None:
        return sum(versions)

    version = int(packet[:3], 2)
    type_ID = int(packet[3:6], 2)
    rest = packet[6:]

    versions.append(version)

    if type_ID == 4:
        r = literal(rest)
        lit = r[0]
        rest = r[1]
        return rest

    else:
        length_type_ID = int(rest[0])
        if length_type_ID: #case number of subpackets
            num_sp = int(rest[1:12], 2)
            subpackets = rest[12:]
            i = 0
            sp_length = 0
            while i < num_sp:
                new_subpackets = parse(subpackets)
                if new_subpackets == None:
                    break
                sp_length += (len(subpackets) - len(new_subpackets))
                subpackets = new_subpackets
                i += 1
            rest = rest[12+sp_length:]
            return rest
            
        else: #case number of bits
            sp_length = int(rest[1:16], 2)
            subpackets = rest[16:16+sp_length]
            while len(subpackets) > 4:
                subpackets = parse(subpackets)
                if subpackets == None:
                    break
            rest = rest[16+sp_length:]
            return rest

def literal(b):
    b_val = ""
    i = 0

    while i < len(b):
        b_val += b[i+1:i+5]
        if b[i] == '0':
            break
        i += 5

    rest_b = b[i+5:]
    n = int(b_val, 2)
    return n, rest_b

def to_hex(packet):
    p = packet.strip()
    return bin(int("1"+p, 16))[3:]

versions = []
if __name__ == "__main__":
    main()
