import psycopg2 as pg
import psycopg2.extensions
from decimal import *
from datetime import datetime
import random
from itertools import permutations
import pages

selectedID = 347786204795292
cardID = 0
addressID = 0

def connect():    
    """ Connect to the PostgreSQL database server """    
    conn = None    
    try:    
        # connect to the PostgreSQL server    
        print('Connecting to the PostgreSQL database...')    
        conn = pg.connect("dbname=airport user=postgres password=123456")    
        print('Connected')
        return conn

    except (Exception, pg.DatabaseError) as error:    
        print(error)    

def loadSQL(conn, schema):
    with open(schema, 'r') as f:
        sql = f.read()
    try:
        with conn.cursor() as curs:
            sql = sql.encode('ascii', 'ignore')
            curs.execute(sql)
            conn.commit()
    except Exception as e:
        conn.rollback()
        raise e

def login(username, password):
    global selectedID
    # Return the user id based on passwd and email
    conn = connect()
    cursor = conn.cursor()

    query = "select email, password, id from customer"
    cursor.execute(query)
    records = cursor.fetchall()
    for i in range(0, len(records)):
        if records[i][0] == username and records[i][1] == password:
            selectedID = records[i][2]
            print(selectedID)
            cursor.close()
            conn.close()
            return True

    return False

def register(firstName, lastName, email, userName, password):
    # Add a tuple that has a unique ID with new email and new passwd
    conn = connect()
    cursor = conn.cursor()
    
    query = "select id, email from customer"
    cursor.execute(query)
    records = cursor.fetchall()
    exists = False
    for s in records:
        if s[1] == email:
            exists = True

    if not exists:
        i = random.randint(0, 999999999999999)

        query = "insert into customer (id, email, password, first_name, last_name, credit_card_number, airport_id) values ("+str(i)+", '"+email+"', '"+password+"', '"+firstName+"', '"+lastName+"', '4905651261779878', 'UKP');" 

        cursor.execute(query)
        conn.commit()

    cursor.close()
    conn.close()

def getCreditByID(cc_id):
    conn = connect()
    cursor = conn.cursor()
    
    try:
        query = "select credit_card_number from credit where user_id = " + str(selectedID) + " and card_id = " + str(cc_id)
        cursor.execute(query)
        ret = cursor.fetchall()[0][0]
        return ret 
    except Exception as e:
        print(e)

    conn.close()
    cursor.close()

def viewCredit(cc, cc_number, street, city, state, country, postal):
    global cardID
    # Open list page
    conn = connect()
    cursor = conn.cursor()
    if cc != '':
        cardID = int(cc)

    conn.set_client_encoding('LATIN1')

    try:
        query = "select * from credit where user_id = " + str(selectedID) + " and card_id = " + str(cardID)
        cursor.execute(query)
        records = cursor.fetchall()
        if cc_number == '':
            cc_number = records[0][1]
        if street == '':
            street = records[0][2]
        if city == '':
            city = records[0][3]
        if state == '':
            state = records[0][4]
        if country == '':
            country = records[0][5]
        if postal == '':
            postal = records[0][6]        
    except:
        pass

    conn.commit()
    
    try:
        query = "insert into credit (user_id, card_id, credit_card_number, street, city, state_name, country, postal_code) values ("+str(selectedID)+", "+str(cardID)+", "+str(cc_number)+", '"+str(street)+"', '"+str(city)+"', '"+str(state)+"', '"+str(country)+"', '"+str(postal)+"')"
        cursor.execute(query)
    except:
        try:
            query = "update credit set credit_card_number="+str(cc_number)+", street='"+street+"', city='"+city+"', state_name='"+state+"', country='"+country+"', postal_code='"+postal+"' where user_id="+str(selectedID)+" and card_id="+str(cardID)
            cursor.execute(query)
        except:
            pass


    conn.commit()

    cursor.close()
    conn.close()
    return (cardID, cc_number, street, city, state, country, postal)

def viewAddr(addr, street, city, state, country, postal):
    global addressID
    # Open list page
    conn = connect()
    cursor = conn.cursor()
    if addr != '':
        addressID = int(addr)

    try:
        query = "select * from addr where user_id = " + str(selectedID) + " and addr_id = " + str(addressID)
        cursor.execute(query)
        records = cursor.fetchall()
        if street == '':
            street = records[0][1]
        if city == '':
            city = records[0][2]
        if state == '':
            state = records[0][3]
        if country == '':
            country = records[0][4]
        if postal == '':
            postal = records[0][5]
    except:
        pass

    try:
        query = "insert into addr (user_id, addr_id, street, city, state_name, country, postal_code) values ("+str(selectedID)+", "+str(addressID)+", '"+str(street)+"', '"+str(city)+"', '"+str(state)+"', '"+str(country)+"', '"+str(postal)+"')"
        cursor.execute(query)
    except:
        try:
            query = "rollback"
            cursor.execute(query)
            query = "update addr set street='"+street+"', city='"+city+"', state_name='"+state+"', country='"+country+"', postal_code='"+postal+"' where user_id='"+str(selectedID)+"' and addr_id="+str(addressID)
            cursor.execute(query)
        except Exception as e:
            print(e)
        
    conn.commit()

    cursor.close()
    conn.close()
    return (addressID, street, city, state, country, postal)

table = []

def updateTable(checkIn, checkOut):
    global table, endIdx
    conn = connect()
    cursor = conn.cursor()

    begDate = datetime.strptime(checkIn, "%m/%d/%Y")
    if checkOut != '':
        endDate = datetime.strptime(checkOut, "%m/%d/%Y")

    query = "select * from airport full join flight on airport_id=home_airport_id;"
    cursor.execute(query)
    table = cursor.fetchall()
    for i, v in enumerate(table):
        curDate = datetime.strptime(v[5]+'-'+v[8], "%m/%d/%Y-%H:%M")
        if curDate > begDate and (checkOut == '' or curDate < endDate):
            return table

def searchRoutes(rem, currIdx, currList, origin, destination, economy):
    global table, endIdx
    result = []

    for x in range(1, rem + 1):
        lists = list(permutations(range(0, len(table)), x))
    
        for currList in lists:
            valid = True
            for i in range(1, len(currList)):
                if table[currList[i - 1]][7] != table[currList[i]][6]:
                    valid = False
            if valid and origin == table[currList[0]][6] and destination == table[currList[len(currList) - 1]][7]:
                result.append(currList)

    return result

def getBookings():
    conn = connect()
    cur = conn.cursor()
    records = []

    try:
        query = "select * from booking where user_id='"+str(selectedID)+"'"
        cur.execute(query)
        records = cur.fetchall()
    except Exception as e:
        print(e)

    return records

    conn.close()
    cur.cose()

def insertBooking(flight_number, airline_code, seatClass, cc):
    conn = connect()
    cur = conn.cursor()

    try:
        query = "insert into booking (user_id, flight_number, airline_code, class, credit_card_type) values ('"+str(selectedID)+"', '"+str(flight_number)+"', '"+str(airline_code)+"', '"+str(seatClass)+"', '"+str(cc)+"')"
        cur.execute(query)
    except Exception as e:
        print(e)

    conn.commit()
    cur.close()
    conn.close()

def deleteBooking(user_id, flight_number):
    conn = connect()
    cur = conn.cursor()

    try:
        query = "delete from booking where user_id='"+user_id+"' and flight_number='"+flight_number+"'"
        cur.execute(query)
    except Exception as e:
        print(e)

    conn.commit()
    cur.close()
    conn.close()

def flightSearch():
    # Open flightSearch page
    conn = connect()
    cur = conn.cursor()

    cur.close()
    conn.close()

if __name__ == '__main__':    
    conn = connect()
    cursor = conn.cursor()

    try:
        loadSQL(conn, "../data/airplane.sql")
    except Exception as e:
        print(e)
    try:
        loadSQL(conn, "../data/airplane-data.sql")
    except Exception as e:
        print(e)

    query = 'select * from credit'
    cursor.execute(query)
    records = cursor.fetchall()

    conn.close()
    cursor.close()
