#!/usr/bin/env python3

import binascii
import argparse

SPACE = ord(' ')


def decode(ciphertexts):

    char_cipher = []
    line_cipher = []
    pad_array = []


    for j in range(0, 64): #64 is number of columns
        #I will create a matrix where, for every line of ciphertexts, I will assign a number to each bities
        for line in ciphertexts:
            for i, elem in enumerate(line, 0):
                if i == j:
                    char_cipher.append(elem)
        line_cipher.append(char_cipher)
        char_cipher = []


    for col in range(0, 64): #I use 64 because is number of columns
        length = len(line_cipher[col]) #for each line I pull out the length. In this way I avoid the "Out of range"

        for i in range(0,length):
            for j in range(0,length):

                if line_cipher[col][i] != line_cipher[col][j]: #I avoid making XOR between same element because the result is 0

                    result = line_cipher[col][i] ^ line_cipher[col][j]

                    if result >= 65:
                        countI = 0
                        countJ = 0
                        for k in range(0,length): #if the result is over 65 I count how many times the result between 'i' xor with another element is over 65
                            xor = line_cipher[col][i] ^ line_cipher[col][k]
                            if xor >= 65:
                                countI += 1

                        for x in range(0, length): #if the result is over 65 I count how many times the result between 'j' xor with another element is over 65
                            xor = line_cipher[col][j] ^ line_cipher[col][x]
                            if xor >= 65:
                                countJ += 1

                        if countI >= countJ:    #I choose the big one because it might be the encoding the of space
                            crack = line_cipher[col][i]
                        else:
                            crack = line_cipher[col][j]

                        break
        pad = crack ^ 32 # I xor between crack and 32 because is value of space
        pad_array.append(pad)

    stampa=""
    for i in range(0,24):  #i print the clear text
        lun=len(ciphertexts[i])
        for j in range(0,lun,1):
            clear_text = ciphertexts[i][j]^pad_array[j]
            clear_tradotto = chr(int(clear_text))
            stampa += (clear_tradotto)
        print(stampa)
        stampa=""







def main():
    parser = argparse.ArgumentParser(description="Many-time Pad Cracker")
    parser.add_argument("--filename", type=str,
                        help="Name of the file containing the ciphertexts (default: ciphertexts.txt)",
                        default="ciphertexts.txt")
    args = parser.parse_args()
    try:
        with open(args.filename) as f:
            ciphertexts = [binascii.unhexlify(line.rstrip()) for line in f]
        cleartexts = [bytearray(b'?' * len(c)) for c in ciphertexts]
    except Exception as e:
        print("Cannot crack {} --- {}".format(args.filename, e))
        raise SystemExit(-1)
    for k in range(max(len(c) for c in ciphertexts)):
        cts = [c for c in ciphertexts if len(c) > k]

    decode(ciphertexts)

    #print("\n".join(c.decode('ascii') for c in cleartexts))


if __name__ == "__main__":
    main()

