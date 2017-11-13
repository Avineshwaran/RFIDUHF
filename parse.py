import serial
import binascii
import sys
import string
import bluetooth
from bluetooth import*
import bluetooth._bluetooth as _bt
import socket
import subprocess
import time


def ParseBluetoothTyre(data):

    hexstr = "aaa14108630005fcaaa1410f630001ba6b09000000002daaa1410f630002ba6d6d0000000094aaa1410f63000356a8cb00000000caaaa1410f63000456a6be00000000bcaaa1410f63000556a7810000000081"
    #hexstr = "aaa14108630005fdaa1410f630002ba6d6d0000000094aaa1410f63000356a8cb00000000caaaa1410f63000456a6be00000000bcaaa1410f63000656a7c500000000c6"
    #aaa1410f63000556a7810000000081  

    
    TPMSIdx = 0
    TPMSIdxx = 0
    TPMS_MAXBUFLEN = 0
    ReadTPMS = 0
    ReadTPMS1 = 0
    ReadTPMS2 = 0
    TPMS_TyreNo = 0
    TPMS_Data = []
    TPMS_Data1 = []
    TPMS_Data2 = []
    
    hexstr1 = [hexstr[i:i+2] for i in range(0,len(hexstr), 2)]
    #print hexstr1
     
    for i in range(len(hexstr1)):
        #print i
        if(hexstr1[i]  == 'aa'):
            TPMSIdx = TPMSIdx + 1
            TPMSIdxx = 0
            TPMSIdxxx = 0
            TPMS_MAXBUFLEN = 0
            ReadTPMS = 1
            ReadTPMS1 = 0
            #print TPMSIdx
            
        elif(ReadTPMS == 1):
            TPMS_Data.append(hexstr1[i])
            TPMSIdxx = TPMSIdxx + 1
            #print str(TPMSIdxx)
             
                    
            if (TPMSIdxx >= 13 ):
                ReadTPMS = 0
                
                #print  TPMS_Data
                #print "TPMS_Data1",TPMS_Data

               
        if TPMSIdx >= 1 & ReadTPMS == 0:
            #TPMS_Data1 = TPMS_Data

            Matrix = [[0 for x in range(TPMSIdx)] for y in range(13)]

            for x in range(TPMSIdx):
                for y in range(13):
                    Matrix[x][y] = TPMS_Data
                    print Matrix
            

            # Creates a list containing 5 lists, each of 8 items, all set to 0
            #w, h = 8, 5;
            #Matrix = [[0 for x in range(w)] for y in range(h)]

            #print Matrix
            #Matrix[0][0] = 1
            #Matrix[6][0] = 3 # error! range... 
            #Matrix[0][6] = 3 # valid

            #print Matrix[0][0] # prints 1
            #x, y = 0, 6 
            #print Matrix[x][y] # prints 3; be careful with indexing! 
            

            
def fun():

    data = "aaa14108630006fdaaa1410f630001ba6b09000000002daaa1410f630002ba6d6d0000000094aaa1410f63000356a8cb00000000caaaa1410f63000456a6be00000000bcaaa1410f63000556a7810000000081aaa1410f63000656a7c500000000c6"
    data = "aaa14108630006fdaaa1410f630001ba6b09000000002daaa1410f630002ba6d6d0000000094aaa1410f63000356a8cb00000000caaaa1410f63000456a6be00000000bcaaa1410f63000556a7810000000081aaa1410f63000656a7c500000000c6"
    hexstr = binascii.b2a_hex(data)

    TPMSID1 = "aa41a1076300f6"
    
    BUID1 = '00:13:EF:C0:02:1E'
    #TpmsTireDataPosition()
    #s = connect_ble(BUID1)

    SID6, L6 = "56a7c5", "06"
    SID2, L2 = "ba6b75", "02"
    #Tpms_Tire_SET_Position1(L6, SID6)
    #Tpms_Tire_SET_Position1(L2, SID2)

    #Tpms_SET_TireID(conn, TMSSET)

    
    
    t = ParseBluetoothTyre(data)
    print t

    #Query_TpmsTireDataPosition(s, TPMSID1)

    

    
    

if __name__ == "__main__":  
    
    fun()           
