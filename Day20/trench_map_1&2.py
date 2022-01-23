
def main(iterations=50):
    with open("Day20\input.txt") as f:
        input = f.readlines()
    alg = input[0]
    image = list(map(lambda x: x.strip(), input[2:]))

    for i in range(iterations):
        image = process(image, alg, i+1)

    n = count_lit(image)
    show(image)
    return n


def process(image, alg, iteration):
    length = len(image[0])
    height = len(image)
    padded_image = pad(image, iteration)
    processed_image = []

    for x in range(length+2):
        processed_row = ""
        for y in range(height+2):
            x_padded = x+1
            y_padded = y+1
            row1 = padded_image[x_padded-1][y_padded-1:y_padded+2]
            row2 = padded_image[x_padded][y_padded-1:y_padded+2]
            row3 = padded_image[x_padded+1][y_padded-1:y_padded+2]
            input = row1+row2+row3
            output = enhance(input, alg)
            processed_row += output
        processed_image.append(processed_row)

    return processed_image

def enhance(input, alg):
    b_str = ""
    d = {".": "0", "#": "1"}

    for pixel in input:
        b_str += d[pixel]
    
    n = int(b_str, 2)
    return alg[n]

def pad(image, iteration):
    size = len(image[0])
    if iteration % 2 == 1:
        padded_line = "." * (size + 4)
    else:
        padded_line = "#" * (size + 4)
    padded_image = [padded_line, padded_line]
    for row in image:
        if iteration % 2 == 1:
            padded_image.append(".." + row + "..")
        else:
            padded_image.append("##" + row + "##")
    padded_image.append(padded_line)
    padded_image.append(padded_line)
    return padded_image

def show(image):
    print("image:")
    for row in image:
        print(row)

def count_lit(image):
    n = 0
    for row in image:
        n += row.count("#")
    return n

if __name__ == "__main__":
    print(main())