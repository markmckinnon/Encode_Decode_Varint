import sys


def encode(number):
    """Pack `number` into varint bytes"""
    counter = 0
    buf = []
    while True:
        towrite = number & 0x7f
        number >>= 7
        if number:
            if counter == 0:
                buf.insert(0, hex(towrite))
                counter = counter + 1
            else:
                towrite = towrite + 128
                hexString = hex(towrite)
                buf.insert(0, hexString)
        else:
            if counter == 0:
                buf.insert(0, hex(towrite))
            else:
                buf.insert(0, hex(towrite+ 128))
            break
    return buf

args = sys.argv[1:]
stringToParse = args[0]
print ("Integer is ==> " + stringToParse)
varInt = encode(int(stringToParse))
print ("Hex Values are ==> " + " ".join(varInt))
