from math import prod

def main():
    with open("Day16\input.txt") as f:
        packet = f.readline()
    #packet = "9C0141080250320F1802104A08" #test data
    values = []
    answer = parse(to_hex(packet), values)
    print(f'{versions = } // sum versions = {sum(versions)}')
    print(f'answer: {answer[1]}')

def parse(packet, values):
    version = int(packet[:3], 2)
    type_ID = int(packet[3:6], 2)
    rest = packet[6:]

    versions.append(version)

    if type_ID == 4:
        r = literal(rest)
        lit = r[0]
        values.append(lit)
        rest = r[1]
        return rest, values

    else:
        length_type_ID = int(rest[0])
        if length_type_ID: #case number of subpackets
            num_sp = int(rest[1:12], 2)
            subpackets = rest[12:]
            i = 0
            sp_length = 0
            while i < num_sp:
                new_subpackets = parse(subpackets, values)
                sp_length += (len(subpackets) - len(new_subpackets[0]))
                subpackets = new_subpackets[0]
                values = new_subpackets[1]
                i += 1
            new_sp = values[0-num_sp:]
            result = do_action(type_ID, new_sp)
            values = values[:0-num_sp]
            values.append(result)
            rest = rest[12+sp_length:]
            return rest, values
            
        else: #case number of bits
            sp_length = int(rest[1:16], 2)
            subpackets = rest[16:16+sp_length]
            num_sp = 0
            while len(subpackets) > 4:
                new_subpackets = parse(subpackets, values)
                subpackets = new_subpackets[0]
                values = new_subpackets[1]
                num_sp += 1
            new_sp = values[0-num_sp:]
            result = do_action(type_ID, new_sp)
            values = values[:0-num_sp]
            values.append(result)
            rest = rest[16+sp_length:]
            return rest, values

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

def do_action(id, values):
    if values == []:
        return

    if id == 0:
        return sum(values)
    elif id == 1:
        return prod(values)
    elif id == 2:
        return min(values)
    elif id == 3:
        return max(values)
    elif id == 5:
        result = 1 if values[0] > values[1] else 0
        return result
    elif id == 6:
        result = 1 if values[0] < values[1] else 0
        return result
    elif id == 7:
        result = 1 if values[0] == values[1] else 0
        return result

versions = []
if __name__ == "__main__":
    main()
