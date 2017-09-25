################################################################
# TMS Integration -09-2017
################################################################

import serial
import binascii
import sys
import bluetooth
from bluetooth import*
import socket
import time


global Tyre1No
global Tyre1ID
global Tyre1Presure
global Tyre1Temp
 
Tyre1No=""
Tyre1ID=""
Tyre1Presure=""
Tyre1Temp = ""

#Tyre2No, Tyre2ID, Tyre2Presure, Tyre2Temp = ""

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

 
def connect_ble(BUID1):
    
    print "performing inquiry..."
    '''
    nearby_devices = bluetooth.discover_devices(lookup_names = True)

    print "found %d devices" % len(nearby_devices)

    for addr, name in nearby_devices:
        print "  %s - %s" % (addr, name)
    '''
    print BUID1

    #serverMACAddress = '00:13:EF:C0:02:1E'
    port = 1
    
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    print "trying to connect to %s on 0x%X" % (BUID1, port)
    s.connect((BUID1, port))
    print "connected to %s on 0x%X" % (BUID1, port)
    
    
    TPMSID1 = TpmsTireDataPosition()
    print binascii.b2a_hex(TPMSID1)
    
    #print "performing Bluetooth Communication..."
    #s.send(TPMSID1)

    #while True:
    #s.send(my_hex)
    print "performing Bluetooth Communication..."
    s.send(TPMSID1)
        
    time.sleep(1)

    data = s.recv(1024)
    #if(len(data) == 0):break
    #print binascii.b2a_hex(data)

    #ParseBluetoothTyre(data)
        
        
    #print binascii.b2a_hex(data)
        

    s.close()

    return data
  


def ParseBluetoothTyre(data):

    #hexStr = "aaa14108630006fdaaa1410f630001ba6b09000000002daaa1410f630002ba6d6d0000000094aaa1410f63000356a8cb00000000caaaa1410f63000456a6be00000000bcaaa1410f63000556a7810000000081aaa1410f63000656a7c500000000c6"
    hexstr = binascii.b2a_hex(data)

    Tyre1No = hexstr[28:30]
    Tyre1ID = hexstr[30:36]
    Tyre1Presure = hexstr[36:42]
    Tyre1Temp = hexstr[42:44]
    print Tyre1No, Tyre1ID, Tyre1Presure, Tyre1Temp
    
    Tyre2No = hexstr[58:60]
    Tyre2ID = hexstr[60:66]
    Tyre2Presure = hexstr[66:72]
    Tyre2Temp = hexstr[72:74]
    print Tyre2No, Tyre2ID, Tyre2Presure, Tyre2Temp

    Tyre3No = hexstr[88:90]
    Tyre3ID = hexstr[90:96]
    Tyre3Presure = hexstr[96:102]
    Tyre3Temp = hexstr[102:104]
    print Tyre3No, Tyre3ID, Tyre3Presure, Tyre3Temp

    Tyre4No = hexstr[118:120]
    Tyre4ID = hexstr[120:126]
    Tyre4Presure = hexstr[126:132]
    Tyre4Temp = hexstr[132:134]
    print Tyre4No, Tyre4ID, Tyre4Presure, Tyre4Temp

    Tyre5No = hexstr[148:150]
    Tyre5ID = hexstr[150:156]
    Tyre5Presure = hexstr[156:162]
    Tyre5Temp = hexstr[162:164]
    print Tyre5No, Tyre5ID, Tyre5Presure, Tyre5Temp

    Tyre6No = hexstr[178:180]
    Tyre6ID = hexstr[180:186]
    Tyre6Presure = hexstr[186:192]
    Tyre6Temp = hexstr[192:194]
    print Tyre6No, Tyre6ID, Tyre6Presure, Tyre6Temp
    
    return Tyre1No, Tyre1ID, Tyre1Presure, Tyre1Temp,Tyre2No, Tyre2ID, Tyre2Presure, Tyre2Temp,Tyre3No, Tyre3ID, Tyre3Presure, Tyre3Temp
            

     

