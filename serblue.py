################################################################
# TPMS Integration 08-09-2017
################################################################

import serial
import binascii
import sys
import bluetooth
from bluetooth import*
import socket
import time

serial = serial.Serial("/dev/ttyS0", baudrate = 9600, timeout = 0.2)


s = 'hello'
data = []
rfidTID_hex = []
rfidTID = []
cksm = []

TID1 = "e2000016351702081640767f"

def RFIDUHFQueryTag():
    

    print("Hello World")
    QueryTag = "040001DB4B"

    my_hex = QueryTag.decode('hex')
    #print my_hex        #
    print binascii.b2a_hex(my_hex)
    serial.write(my_hex)

    #print " ".join(hex(ord(n)) for n in my_hex)


def ParseRFIDResponse():
    
    data = serial.readline()
    #print data
    
    if(data[3] == '\x01'):
        print "H1111111111"
        
        #rfid = binascii.b2a_hex(data)
        rfidTID_hex = binascii.b2a_hex(data)
        print rfidTID_hex
        rfidTID = rfidTID_hex [12:36]
        print rfidTID

        if rfidTID == TID1:
            print "Hello"
        
        '''
        print "************************"
        rfidTID1_hex = binascii.hexlify(data)
        print rfidTID_hex
        rfidTID1 = rfidTID1_hex [12:37]
        print rfidTID1
        print "************************"
        '''
        
        
        
        #print(" ".join("{:02x}".format(ord(c)) for c in rfidTID))
        #print(binascii.unhexlify(data[3]))        
        #print binascii.unhexlify('7061756c')
        #print(binascii.unhexlify(b"437c2123"))
        #print(binascii.unhexlify(data))
        #print data
        #data_con = bytes.fromhex(data)
        #print data_con
        #x = ''.join(chr(int(data[i:i+2], 16)) for i in range(0, len(data), 2))

def bluetoothEnquiry():
    
    
    print "performing inquiry..."
    '''
    nearby_devices = bluetooth.discover_devices(lookup_names = True)

    print "found %d devices" % len(nearby_devices)

    for addr, name in nearby_devices:
        print "  %s - %s" % (addr, name)
    '''

    serverMACAddress = '00:13:EF:C0:02:1E'
    port = 1
    
    #s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    print "trying to connect to %s on 0x%X" % (serverMACAddress, port)
    s.connect((serverMACAddress, port))

    TPMSID1 = TpmsTireDataPosition()
    print binascii.b2a_hex(TPMSID1)
    
    print "performing Bluetooth Communication..."
    s.send(TPMSID1)

    while 1:
        #sock.send(my_hex)

        time.sleep(1)

        data = s.recv(1024)
        if(len(data) == 0): break

        print binascii.b2a_hex(data)
    

    s.close()
    

# TPMS Bluetooth FMS request TPMS to send all recorded tyres data

def TpmsTireDataPosition():
    #TpmsModuleQuery = ['\xAA', '\x41', '\xA1', '\x07', '\x63', '\x00']
    #TpmsModuleQuery = ['AA', '41', 'A1', '07', '63', '00']
    #TpmsModuleQuery = ["AA", "41", "A1", "07", "63", "00"]

    
    TpmsModuleQuery = ["\xAA", "\x41", "\xA1", "\x07", "\x63",  "\x00"]
    TpmsModuleQueryID = "AA41A1076300"
    
    #print TpmsModuleQuery
    TpmsCksm = TpmsCalcChecksum(TpmsModuleQuery)
    #print TpmsCksm

    #Append checksum to the Query List
    TPMSQueryAllTyre = TpmsModuleQueryID + TpmsCksm
    #print TPMSQueryAllTyre

    my_hex_TPMS = TPMSQueryAllTyre.decode('hex')
    print my_hex_TPMS       
    #print binascii.b2a_hex(my_hex_TPMS)


    #serial.write(my_hex_TPMS)
    
    
    #print unhexlify(TpmsCksm)
    #append checksum to the Query List
    #TpmsModuleQuery.append(TpmsCksm)
    #print TpmsModuleQuery

    return my_hex_TPMS   
    

# TPMS Bluetooth Calculate Checksum

def TpmsCalcChecksum(TpmsModuleQuery1):

    count = len(TpmsModuleQuery1)
    #print TpmsModuleQuery1

    
    i = 0
    cksm = 0
    while (i < count-1):
        #print(TpmsModuleQuery1[i])
        val = binascii.b2a_hex(TpmsModuleQuery1[i])
        cksm += int (val, 16)

      
        cksm1 = hex(cksm).split('x')[-1]
        #cksm1 = hex(cksm)
        #print cksm1

        i += 1
        
    #print cksm1
    high, low = cksm1[:1], cksm1[1:3]
    #print(high, low)

    return low
    

# TPMS Bluetooth Calculate Checksum
'''
def TpmsCalcChecksum(TpmsModuleQuery1):
    cksm = []
    cnt = len(TpmsModuleQuery1)
    print TpmsModuleQuery1
    
    while(cnt >= 0):
        cksm += TpmsModuleQuery1[cnt]
        cnt= cnt-1
        print TpmsModuleQuery1[cnt]
    #for counter in range(cnt, 0, -1):
     #   print counter
        #cksm = cksm+TpmsModuleQuery1[counter]
        #print TpmsModuleQuery1[counter]
     
    #for i in range(len(TpmsModuleQuery1)):
        #print(TpmsModuleQuery1[i])
      
    print cksm
    return cksm
'''
def ParseBluetoothTyre():

    hexStr = "aaa14108630006fdaaa1410f630001ba6b09000000002daaa1410f630002ba6d6d0000000094aaa1410f63000356a8cb00000000caaaa1410f63000456a6be00000000bcaaa1410f63000556a7810000000081aaa1410f63000656a7c500000000c6"

    bytes = []

    hexStr = ''.join( hexStr.split(" ") )
    #print hexStr
    
    for i in range(0, len(hexStr), 2):
        bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )

    print   ''.join( bytes )
    
    print data 

def fun():
    #while 1:
        #RFIDUHFQueryTag()
        #ParseRFIDResponse()
        #bluetoothEnquiry()
        #TpmsTireDataPosition()
        ParseBluetoothTyre()



if __name__ == "__main__":  
    
    fun()
