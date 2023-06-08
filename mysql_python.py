import datetime
from datetime import datetime, date
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# By John Tu CPSC 332-08

# The following section below is the reference template for inserting queries.
#new_Artist = """INSERT INTO ARTIST (ArtistName, Phone, Address,
#                   Birthplace, ArtistAge, ArtStyle)
#                   VALUES
#                   (,,,,,)"""
#new_Art_Work = """INSERT INTO ART_WORK (ArtistName, ArtTitle, ArtType,
#                   DateCreated, DateAcquired, Price, ArtLocation)
#                   VALUES
#                   (,,,,,,)"""
#new_Customer = """INSERT INTO CUSTOMER (CustNumber, CustPhone, ArtPref)
#                   VALUES
#                   (,,)"""
#new_Art_Show = """INSERT INTO ART_SHOW (ArtistName, Date_and_Time,
#                   Location, ContactName, ContactPhone)
#                   VALUES
#                   (,,,,)"""

try:
    # Connect to the MySQL Server if possible.
    newConnect = mysql.connector.connect(host="127.0.0.1",
                                   user="root",
                                   password="T1t@n1umus",
                                   auth_plugin="mysql_native_password",
                                   database="GALLERY")
    if newConnect.is_connected():
        # Display the following information below after a successful connection.
        db_Info = newConnect.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        newCursor = newConnect.cursor()
        newCursor.execute("select database();")
        thisRecord = newCursor.fetchone()
        print("Connected to database: ", thisRecord)

        print("Now inserting the data into the database...")
        # Be sure to use string formatting to avoid repetition.
        insert_Artist = """INSERT INTO ARTIST (ArtistName, Phone, Address,
                   Birthplace, ArtistAge, ArtStyle)
                   VALUES
                   (%s,%s,%s,%s,%s,%s)"""
        insert_Art_Work = """INSERT INTO ART_WORK (ArtistName, ArtTitle, ArtType,
                   DateCreated, DateAcquired, Price, ArtLocation)
                   VALUES
                   (%s,%s,%s,%s,%s,%s,%s)"""
        insert_Customer = """INSERT INTO CUSTOMER (CustNumber, CustPhone, ArtPref)
                   VALUES
                   (%s,%s,%s)"""
        insert_Art_Show = """INSERT INTO ART_SHOW (ArtistName, Date_and_Time,
                   Location, ContactName, ContactPhone)
                   VALUES
                   (%s,%s,%s,%s,%s)"""
        
        new_Artist1 = ("Randy Brasher","779-337-9837","117 Elder Ln",
                   "Rockford",60,"Classical")
        new_Artist2 = ("Ripley Faulkner","814-410-5371","789 Lee Ave",
                   "Erie",55,"Modern")
        new_Art_Work1 = ("Randy Brasher","Many Hills","Watercolor",
                         datetime(int(1991),int(5),int(30)),
                         datetime(int(2011),int(10),int(3)),
                         3500,"Front Room")
        new_Art_Work2 = ("Randy Brasher","Family Portrait","Oil Paint",
                         datetime(int(1994),int(11),int(7)),
                         datetime(int(2016),int(5),int(12)),
                         1800,"Basement")
        new_Art_Work3 = ("Ripley Faulkner","Stairwells","Acrylic",
                         datetime(int(2003),int(2),int(4)),
                         datetime(int(2011),int(12),int(15)),
                         3850,"Foyer")
        new_Art_Work4 = ("Ripley Faulkner","New Age","Pastel",
                         datetime(int(2010),int(10),int(14)),
                         datetime(int(2013),int(9),int(15)),
                         1800,"Retreat")
        new_Customer1 = (183,"764-802-8576", "Classical")
        new_Customer2 = (881,"534-888-6727", "Modern")
        new_Customer3 = (230,"840-382-2016", None)
        new_Art_Show1 = ("Randy Brasher","April 22 2019 11:00 AM",
                         "Rochester","Lewin Everett","584-435-3675")
        new_Art_Show2 = ("Ripley Faulkner","July 7 2015 11:30 AM",
                         "Chicago","Pete Wood","847-593-2338")

        newCursor.execute(insert_Artist, new_Artist1)
        newCursor.execute(insert_Artist, new_Artist2)
        newCursor.execute(insert_Art_Work, new_Art_Work1)
        newCursor.execute(insert_Art_Work, new_Art_Work2)
        newCursor.execute(insert_Art_Work, new_Art_Work3)
        newCursor.execute(insert_Art_Work, new_Art_Work4)
        newCursor.execute(insert_Customer, new_Customer1)
        newCursor.execute(insert_Customer, new_Customer2)
        newCursor.execute(insert_Customer, new_Customer3)
        newCursor.execute(insert_Art_Show, new_Art_Show1)
        newCursor.execute(insert_Art_Show, new_Art_Show2)
        print("Data insertion complete.\n")

        # When displaying the database, run a for loop through each row.
        print("Displaying the database...")
        artist_select = "select * from ARTIST"
        art_work_select = "select * from ART_WORK"
        customer_select = "select * from CUSTOMER"
        art_show_select = "select * from ART_SHOW"
        
        newCursor.execute(artist_select)
        thisRecord = newCursor.fetchall()
        print("\nNow printing artist record")
        for row in thisRecord:
            print("Name: ", row[0])
            print("Phone: ", row[1])
            print("Address: ", row[2])
            print("Birthplace: ", row[3])
            print("Age: ", row[4])
            print("Art Style: ", row[5], "\n")

        newCursor.execute(art_work_select)
        thisRecord = newCursor.fetchall()
        print("\nNow printing artwork record")
        for row in thisRecord:
            print("Artist: ", row[0])
            print("Title: ", row[1])
            print("Art Type: ", row[2])
            print("Date Created: ", row[3])
            print("Date Acquired: ", row[4])
            print("Price: ", row[5])
            print("Location: ", row[6], "\n")

        newCursor.execute(customer_select)
        thisRecord = newCursor.fetchall()
        print("\nNow printing customer record")
        for row in thisRecord:
            print("Number: ", row[0])
            print("Phone: ", row[1])
            print("Art Preference: ", row[2], "\n")

        newCursor.execute(art_show_select)
        thisRecord = newCursor.fetchall()
        print("\nNow printing art show record")
        for row in thisRecord:
            print("Artist: ", row[0])
            print("Date & Time: ", row[1])
            print("Location: ", row[2])
            print("Contact Name: ", row[3])
            print("Contact Phone: ", row[4], "\n")

        print("\nDisplaying list of art work from artist Ripley Faulkner...")
        art_work_select2 = "select * from ART_WORK where ArtistName = 'Ripley Faulkner'"
        newCursor.execute(art_work_select2)
        thisRecord = newCursor.fetchall()
        for row in thisRecord:
            print("Artist: ", row[0])
            print("Title: ", row[1])
            print("Art Type: ", row[2])
            print("Date Created: ", row[3])
            print("Date Acquired: ", row[4])
            print("Price: ", row[5])
            print("Location: ", row[6], "\n")

        print("\nSorting the list of art work by price...")
        art_work_sort = "select ArtTitle, ArtistName, Price from ART_WORK order by Price"
        newCursor.execute(art_work_sort)
        thisRecord = newCursor.fetchall()
        for row in thisRecord:
            print("Title: ", row[0])
            print("Artist: ", row[1])
            print("Price: ", row[2], "\n")
            
# If something unexpected occured, display the error message and explain why.
except Error as e:
    print("An exception has occured", e)

# Regardless of the outcome, be sure to close connection afterwards.
finally:
    if (newConnect.is_connected()):
        newCursor.close()
        newConnect.close()
        print("MySQL connection is closed")
        
