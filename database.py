import sqlite3
from sqlite3 import Error
import __main__
from pip._vendor.pkg_resources import null_ns_handler


#def create_database(): 
def create_connection(db_file):
    """Create a database connection to the DB file test.db"""
    try:
        conn = sqlite3.connect(db_file)
        print (" Create a connection to DB ")
        return conn
    except Error as e:
        print (e)
        
    return None

def create_teble(conn, create_table_sql):
    """create a table from the create_table_sql statement"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print (" Create a Table in DB ")
    except Error as e:
        print (e)       
                
def create_insert_vehicle(conn, vehicle_list):
    """ Create a insert row in the vehicle table 
    param: conn:
    param: bus_no
    param: device_id
    param: RFID_TAG_id
    param: bluetooth_id """
    
    sql = '''INSERT INTO vehicle(bus_no, device_id, RFID_TAG_id, bluetooth_id)
            VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql,vehicle_list)
    print "Create a insert row in the vehicle table"
    return cur.lastrowid

def create_insert_tyre_sensor_id(conn, task):
    """ Create a Insert in tyre_sensor_id table
    param: conn:
    param: bus_no
    param: bluetooth_id
    param: sensor_FL_1, sensor_FR_2, sensor_RLI_3, sensor_RLO_4, sensor_RRI_5, sensor_RRO_6
    param: status_id"""
    
    sql = '''INSERT INTO tyre_sensor_id(bus_no, bluetooth_id, sensor_FL_1, sensor_FR_2, sensor_RLI_3, sensor_RLO_4, sensor_RRI_5, sensor_RRO_6, status_id)
            VALUES(?,?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql,task)
    #print ("Create Insert in tyre_sensor_id")
    return cur.lastrowid


def delete_ID_tyre_sensor_id(conn, deleteID):
    """Delete Row in TASK table based on ID"""
    
    sql = 'DELETE FROM TASK WHERE id=?'
    
    cur = conn.cursor()
    cur.execute(sql, (deleteID,))
    return cur.lastrowid

def delete_all_vehicle(conn):
    """Delete All Row in vehicle table"""
    
    sql = 'DELETE FROM vehicle'
    
    cur = conn.cursor()
    cur.execute(sql)
    return cur.lastrowid
    
def update_table_vehicle(conn, task):
    """
    update priority, begin_date, and end date of a task
    param conn:
    param task:
    return: project id
    """
    sql = ''' UPDATE vehicle
              SET bus_no = ? ,
                  device_id = ?,
                  RFID_TAG_id = ? ,
                  bluetooth_id = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)

def update_table_vehicle_RFID(conn, task):
    """
    update priority, begin_date, and end date of a task
    param conn:
    param task:
    return: project id
    """
    sql = ''' UPDATE vehicle
              SET RFID_TAG_id = ? 
              WHERE bus_no = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)

def update_table_tyre_sensor_id(conn, update_sensor):
    """Update the table tyre_sensor_id to other format"""
    
    sql = ''' UPDATE tyre_sensor_id
              SET   bus_no = ?,
                    bluetooth_id = ?,
                    tyre_sensor_FL_1 = ?,
                    tyre_sensor_FR_2 = ?,
                    tyre_sensor_RLI_3 = ?,
                    tyre_sensor_RLO_4 = ?,
                    tyre_sensor_RRI_5 = ?,
                    tyre_sensor_RLO_6 = ?,
                    status_id = ?
            '''
    
    cur = conn.cursor()
    cur.execute(sql, update_sensor)
    return cur.lastrowid
    
    
def select_DeviceDetails_by_rfiduid(conn, rfiduid1):
    """
    Query tasks by priority
    param conn: the Connection object
    param rfiduid:
    """
    print (" select_DeviceDetails_by_id ")
    cur = conn.cursor()
    cur.execute("SELECT vehId, vehName, BUID, RFUID FROM DeviceDetails WHERE RFUID=?",(rfiduid1,))
 
    rows = cur.fetchall()
    vehDetials = None;
    for row in rows:
        vehDetials = row
        
    return vehDetials
    #def select_DeviceDetails_by_rfiduid(conn, rfiduid1):
    
    
def select_TyreDetails_by_VehId(conn, VehId1):
    """
    Query tasks by priority
    param conn: the Connection object
    param rfiduid:
    """
    TyreDetials = []
    print (" select_TireDetails_by_VehId ")
    cur = conn.cursor()
    cur.execute("SELECT sensorUID, tirePosition FROM TireDetails WHERE vehId=?",(VehId1,))
 
    rows = cur.fetchall()
    #TyreDetials = None;
    for row in rows:
        TyreDetials = row
        print TyreDetials
        
    return TyreDetials
    #def select_DeviceDetails_by_rfiduid(conn, rfiduid1):
    
    
    
def main():
    
    database = "D:/Aquire/sqlite/Sample.db"
    print (" Create a connection ")
    
    sql_create_table_vehicle = """CREATE TABLE IF NOT EXISTS vehicle (
                                id         integer PRIMARY KEY,
                                bus_no     text,
                                device_id  text,
                                RFID_TAG_id    text,
                                bluetooth_id   text
                                ); """
    '''
    sql_create_table_tyre_sensor_id = """CREATE TABLE IF NOT EXISTS tyre_sensor_id (
                                    id integer PRIMARY KEY,
                                    bus_no    text,
                                    bluetooth_id text,
                                    tyre_sensor_FL_1    text,
                                    tyre_sensor_FR_2    text,
                                    tyre_sensor_RLI_3    text,
                                    tyre_sensor_RLO_4    text,
                                    tyre_sensor_RRI_5    text,
                                    tyre_sensor_RLO_6    text,
                                    status_id integer NOT NULL
                                );"""
    '''
    #create a connection to database
    conn = create_connection(database)
    '''
    if conn is not None:
        #create vehicle table
        create_teble(conn, sql_create_table_vehicle)
        #create Sensor_id table
        #create_teble(conn, sql_create_table_tyre_sensor_id)
    else:
        print ("Error Cannot Create a connection ")
    '''
    
    with conn:
        #vehicle_detail = ('7458', 'aaaaa', '11111111', 'AAAAAAAA')
        
        #create_insert_vehicle(conn, vehicle_detail)
        ''' 
        #create Tasks
        task1 = ("7458","AAAAAAAA", "aaaaaa", "bbbbbb", "cccccc", "dddddd", "eeeeee", "ffffff", '1')
        
        create_insert_tyre_sensor_id(conn, task1)

        #update_vehicle_detail =  ('7458', 'aaaaa', '11111111', 'AAAAAAAA')
        
        #create_insert_vehicle(conn, vehicle_detail)
        
        #update_table_vehicle(conn, update_vehicle_detail)
        
        #update_tyre_sensor_id = (2, '2015-01-04', '2015-01-06')
         
        #delete_all_vehicle_detail(conn)
        '''
        #print("1. Query vehicle by id:")
        #select_vehicle_by_id(conn, 1)
        #select_tms_rfid_by_rfiduid(conn, RFID UID4)
    
if __name__ == '__main__':
    main()
     
    
    








