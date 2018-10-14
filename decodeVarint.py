import sys

def readVarintRecords(StringToParse, stringLength):
    recordsRead = 0
    stringPosition = 0
    # Refactor this for variable names
    varint = int(stringToParse[stringPosition: stringPosition + 2], 16)
    stringPosition = stringPosition + 2
    recordsRead = recordsRead + 1
    if varint >= 128:
        tempBinaryVarint = '{0:08b}'.format(varint)
        stringBinaryVarint = tempBinaryVarint[1:]
        print (stringBinaryVarint)
        # stringSerialType = serialType
        if stringPosition <= stringLength:
            varint = int(stringToParse[stringPosition: stringPosition + 2], 16)
            stringPosition = stringPosition + 2
            recordsRead = recordsRead + 1
            while True:
                if varint >= 128:
                    tempBinaryVarint = '{0:08b}'.format(varint)
                    stringBinaryVarint = stringBinaryVarint + tempBinaryVarint[1:]
                    print (stringBinaryVarint)
                    # stringSerialType = stringSerialType + serialType
                    if stringPosition >= stringLength:
                        break
                    varint = int(stringToParse[stringPosition: stringPosition + 2], 16)
                    stringPosition = stringPosition + 2
                    recordsRead = recordsRead + 1
                else:
                    tempBinaryVarint = '{0:08b}'.format(varint)
                    stringBinaryVarint = stringBinaryVarint + tempBinaryVarint[1:]
                    print (stringBinaryVarint )
                    break
        return int(stringBinaryVarint, base=2), recordsRead
    else:
        return varint, recordsRead

args = sys.argv[1:]
stringToParse = args[0]
varInt = readVarintRecords(stringToParse, len(stringToParse))
print ("Integer is ==> " + str(varInt[0]))
