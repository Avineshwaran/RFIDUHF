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
tag_id = []

database = "/opt/Aquire/sqlite/Sample.db"
TID1 = "e2000016351702081640767f"
#tag_id = "RFID 1"

# Start Query the DB with RFID TID
def db_DeviceDetails_by_rfiduid():

    print("Create a database connection to the DB file .db")
    conn = db.create_db_connection(database)
    
    print("Query the database to read Vehicle Details by RFUID")
    vehDetail = db.select_DeviceDetails_by_rfiduid(conn, tag_id)

    if (vehDetail != None):
        vehID = vehDetail[0]
        vehName = vehDetail[1]
        BUID = vehDetail[2]
        RFUID = vehDetail[3]

        print vehID, vehName, BUID, RFUID

    return vehID, vehName, BUID, RFUID
        

def fun():
    print("Main Function")

    print("RFID Module Read TAG ID Function")
    tag_id = rfid.RFIDUHFQueryTag()
    
    vehID, vehName, BUID, RFUID = db_DeviceDetails_by_rfiduid()
    
    

if __name__ == "__main__":  
    
    fun()
    
        
