################################################################
# TPMS Integration -09-2017
################################################################

import serial
import binascii
import sys
import bluetooth
from bluetooth import*
import socket
import time
import sqlite3
from sqlite3 import Error
import __main__
from pip._vendor.pkg_resources import null_ns_handler

import db
import rfid

#Variable Decleration
s = 'hello'
data = []
rfidTID_hex = []
rfidTID = []
cksm = []
vehID = 0
vehName = ""
BUID = ""
RFUID = ""
#tag_id = ""

database = "/opt/Aquire/sqlite/Sample.db"
TID1 = "e2000016351702081640767f"
tag_id = "RFUID 1"
vehID = 24

# Start Query the DB with RFID TID
def db_DeviceDetails_by_rfiduid():

    print("Create a database connection to the DB file .db")
    conn = db.create_db_connection(database)
    
    #print tag_id
    print("Query the database to read Vehicle Details by RFUID")
    #vehDetail = db.select_DeviceDetails_by_rfiduid(conn, "RFID 1")

    with conn:
        vehDetail = db.select_DeviceDetails_by_rfiduid(conn, tag_id)

    if (vehDetail != None):
        vehID = vehDetail[0]
        vehName = vehDetail[1]
        BUID = vehDetail[2]
        RFUID = vehDetail[3]

        #print vehID, vehName, BUID, RFUID

    return vehID, vehName, BUID, RFUID


# Start Query the DB with vehID to get Tyre Details
def db_DeviceDetails_by_vehID(vehID1):

    print("Create a database connection to the DB file .db")
    conn = db.create_db_connection(database)
    
    #print vehID
    print("Query the database to read Tyre Details by vehID")
    #vehDetail = db.select_DeviceDetails_by_rfiduid(conn, vehID)

    with conn:
        TyreDetail = db.select_TyreDetails_by_VehId(conn, 24)
        #print TyreDetail
    if (TyreDetail != None):

     
        if(TyreDetail[0] != None):
            Tyre_row1 = TyreDetail[0]

            SID1, L1 = Tyre_row1[0], Tyre_row1[1]
            print SID1, L1
            
        if(TyreDetail[1] != None):
            Tyre_row2 = TyreDetail[1]

            SID2, L2 = Tyre_row2[0], Tyre_row2[1]
            print SID2, L2
            
        if(TyreDetail[2] != None):
            Tyre_row3 = TyreDetail[2]

            SID3, L3 = Tyre_row3[0], Tyre_row3[1]
            print SID3, L3

        if(TyreDetail[3] != None):
            Tyre_row4 = TyreDetail[3]

            SID4, L4 = Tyre_row4[0], Tyre_row4[1]
            print SID4, L4

        if(TyreDetail[4] != None):
            Tyre_row5 = TyreDetail[4]

            SID5, L5 = Tyre_row5[0], Tyre_row5[1]
            print SID5, L5

        if(TyreDetail[5] != None):
            Tyre_row6 = TyreDetail[5]

            SID6, L6 = Tyre_row6[0], Tyre_row6[1]
            print SID6, L6
       
        
    
    print("Close a database connection to the DB file .db")
    conn.close()
    
    #return vehID, vehName, BUID, RFUID
        
# Start Connecting the Socket by BUID
def Connect_Socket_Bluetooth_by_BUID(BUID):

    print("Create a database connection to the DB file .db")
    conn = db.create_db_connection(database)
    
    #print tag_id
    print("Query the database to read Vehicle Details by RFUID")
    #vehDetail = db.select_DeviceDetails_by_rfiduid(conn, "RFID 1")

    with conn:
        vehDetail = db.select_DeviceDetails_by_rfiduid(conn, tag_id)

    if (vehDetail != None):
        vehID = vehDetail[0]
        vehName = vehDetail[1]
        BUID = vehDetail[2]
        RFUID = vehDetail[3]

        #print vehID, vehName, BUID, RFUID

    return vehID, vehName, BUID, RFUID

def fun():
    print("Main Function")

    #print("RFID Module Read TAG ID Function")
    #tag_id = rfid.RFIDUHFQueryTag()
    
    #vehID, vehName, BUID, RFUID = db_DeviceDetails_by_rfiduid()

    #print "Main: ", vehID, vehName, BUID, RFUID
    vehID=24
    if (vehID != None):
        print("Query the Database to read Tyre Details, Sensor ID, Position by vehID")
        db_DeviceDetails_by_vehID(vehID)

    
    if (BUID != None):
        print("Connect socket RFCOMM to Bluetooth Controller by vehID")
        Connect_Socket_Bluetooth_by_BUID(BUID)    

if __name__ == "__main__":  
    
    fun()
    
        

    
        
