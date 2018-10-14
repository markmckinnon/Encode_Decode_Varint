import sys
import os
#import time
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import Qt
import ntpath
#from Database import SQLiteDb
from SQLiteInternals import SQLiteInternals

qtCreatorFile = "encodedecodevarint.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Setup Buttons
        self.encodeBTN.clicked.connect(self.encodeVarint)
        self.decodeBTN.clicked.connect(self.decodeVarint)

    def decodeVarint(self):

        stringToParse = self.varIntLE.text()
        self.decodedInt.setText("")
        varInt, recordsRead = self.readVarintRecords(str(stringToParse), len(stringToParse))
        self.decodedInt.setText(str(varInt))

    def encodeVarint(self):
        print("here")
        stringToParse = self.intLE.text()
        self.encodevarint.setText("")
        varInt = self.encodeVarInt(int(str(stringToParse)))
        stringVarInt = " ".join(varInt)
        self.encodevarint.setText(str(stringVarInt))

    def readVarintRecords(self, stringToParse, stringLength):
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

    def encodeVarInt(self, number):
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


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())