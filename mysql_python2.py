import datetime
from datetime import datetime, date
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

#By John Tu CPSC 332-08
nArtist = 0
nArtwork = 0
nCustomer = 0
nArtShow = 0
isValid = False
isValid2 = False

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

        # Be sure to use string formatting template below to avoid unwanted repetition.
        insert_Artist = """INSERT INTO ARTIST (ArtistName, Phone, Address,
                   Birthplace, ArtistAge, ArtStyle)
                   VALUES
                   (%s,%s,%s,%s,%s,%s)"""
        insert_Artwork = """INSERT INTO ART_WORK (ArtistName, ArtTitle, ArtType,
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
        
        # Part 1: Ask the user to input the values into the database.
        # Run a for loop after asking how many number of each entries to be inserted.
        print("Enter the number of artists")
        nArtist = input()
        i = 1
        while i <= int(nArtist):
            print("Enter the artist name")
            artistName = input()
            print("Enter the phone number")
            artistPhone = input()
            print("Enter the address")
            artistAddress = input()
            print("Enter the birthplace")
            artistBirth = input()
            print("Enter the artist's age")
            artistAge = input()
            print("Enter the art style")
            artistStyle = input()
            
            print("Now inserting all the data into the query...")
            newArtist = (artistName, artistPhone, artistAddress,
                         artistBirth, artistAge, artistStyle)
            newCursor.execute(insert_Artist, newArtist)
            newConnect.commit()
            print("Insertion complete.\n")
            i += 1

        print("Enter the number of artworks")
        nArtwork = input()
        i = 1
        while i <= int(nArtwork):
            print("Enter the artist name")
            artworkName = input()
            print("Enter the art title")
            artworkTitle = input()
            print("Enter the art type")
            artworkType = input()
            print("Enter the date of creation")
            artworkCreate = input()
            print("Enter the date of acquirement")
            artworkAcquire = input()
            print("Enter the price")
            artworkPrice = input()
            print("Enter the art location")
            artworkLocation = input()
            
            print("Now inserting all the data into the query...")
            newArtwork = (artworkName, artworkTitle, artworkType, artworkCreate,
                          artworkAcquire, artworkPrice, artworkLocation)
            newCursor.execute(insert_Artwork, newArtwork)
            newConnect.commit()
            print("Insertion complete.\n")
            i += 1

        print("Enter the number of customers")
        nCustomer = input()
        i = 1
        while i <= int(nCustomer):
            print("Enter the customer number")
            custNumber = input()
            print("Enter the customer phone")
            custPhone = input()
            print("Enter the art preference")
            custPref = input()
            
            print("Now inserting all the data into the query...")
            newCustomer = (custNumber, custPhone, custPref)
            newCursor.execute(insert_Customer, newCustomer)
            newConnect.commit()
            print("Insertion complete.\n")
            i += 1

        print("Enter the number of art shows")
        nArtShow = input()
        i = 1
        while i <= int(nArtShow):
            print("Enter the artist name")
            showArtist = input()
            print("Enter the date and time")
            showDateTime = input()
            print("Enter the location")
            showLocation = input()
            print("Enter the contact name")
            showContact = input()
            print("Enter the contact's phone")
            showPhone = input()
            
            print("Now inserting all the data into the query...")
            newArtShow = (showArtist, showDateTime, showLocation,
                          showContact, showPhone)
            newCursor.execute(insert_Art_Show, newArtShow)
            newConnect.commit()
            print("Insertion complete.\n")
            i += 1

        # Run a for loop while displaying the database to the user.
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

            
        # Part 2: Ask the user to choose which record to sort.
        while isValid == False:
            print("Select which record to sort.")
            print("1: Artist")
            print("2: Artwork")
            print("3: Customer")
            print("4: Art show")
            choice = input()

            if int(choice) == 1:
                isValid = True
                while isValid2 == False:
                    print("How do you want the artist record sorted by?")
                    print("1: Artist name")
                    print("2: Artist phone")
                    print("3: Address")
                    print("4: Birthplace")
                    print("5: Age")
                    print("6: Art style")
                    choice2 = input()

                    if int(choice2) == 1:
                        isValid2 = True
                        print("Sorting artist record by name.")
                        querySort = "select * from ARTIST order by ArtistName"
                    elif int(choice2) == 2:
                        isValid2 = True
                        print("Sorting artist record by phone.")
                        querySort = "select * from ARTIST order by Phone"
                    elif int(choice2) == 3:
                        isValid2 = True
                        print("Sorting artist record by address.")
                        querySort = "select * from ARTIST order by Address"
                    elif int(choice2) == 4:
                        isValid2 = True
                        print("Sorting artist record by birthplace.")
                        querySort = "select * from ARTIST order by Birthplace"
                    elif int(choice2) == 5:
                        isValid2 = True
                        print("Sorting artist record by age.")
                        querySort = "select * from ARTIST order by ArtistAge"
                    elif int(choice2) == 6:
                        isValid2 = True
                        print("Sorting artist record by art style.")
                        querySort = "select * from ARTIST order by ArtStyle"
                    else:
                        print("Invalid choice. Please re-enter.")

                    newCursor.execute(querySort)
                    thisRecord = newCursor.fetchall()
                    for row in thisRecord:
                        print("Name: ", row[0])
                        print("Phone: ", row[1])
                        print("Address: ", row[2])
                        print("Birthplace: ", row[3])
                        print("Age: ", row[4])
                        print("Art Style: ", row[5], "\n")
                        
            elif int(choice) == 2:
                isValid = True
                while isValid2 == False:
                    print("How do you want the artwork record sorted by?")
                    print("1: Artist name")
                    print("2: Artwork title")
                    print("3: Art type")
                    print("4: Date of creation")
                    print("5: Date of acquirement")
                    print("6: Price")
                    print("7: Location of art")
                    choice2 = input()

                    if int(choice2) == 1:
                        isValid2 = True
                        print("Sorting artwork record by artist name.")
                        querySort = "select * from ART_WORK order by ArtistName"
                    elif int(choice2) == 2:
                        isValid2 = True
                        print("Sorting artwork record by artwork title.")
                        querySort = "select * from ART_WORK order by ArtTitle"
                    elif int(choice2) == 3:
                        isValid2 = True
                        print("Sorting artwork record by art type.")
                        querySort = "select * from ART_WORK order by ArtType"
                    elif int(choice2) == 4:
                        isValid2 = True
                        print("Sorting artwork record by creation date.")
                        querySort = "select * from ART_WORK order by DateCreated"
                    elif int(choice2) == 5:
                        isValid2 = True
                        print("Sorting artwork record by acquirement date.")
                        querySort = "select * from ART_WORK order by DateAcquired"
                    elif int(choice2) == 6:
                        isValid2 = True
                        print("Sorting artwork record by price.")
                        querySort = "select * from ART_WORK order by Price"
                    elif int(choice2) == 7:
                        isValid2 = True
                        print("Sorting artwork record by art location.")
                        querySort = "select * from ART_WORK order by ArtLocation"
                    else:
                        print("Invalid choice. Please re-enter.")
                        
                    newCursor.execute(querySort)
                    thisRecord = newCursor.fetchall()
                    for row in thisRecord:
                        print("Artist: ", row[0])
                        print("Title: ", row[1])
                        print("Art Type: ", row[2])
                        print("Date Created: ", row[3])
                        print("Date Acquired: ", row[4])
                        print("Price: ", row[5])
                        print("Location: ", row[6], "\n")
                        
            elif int(choice) == 3:
                isValid = True
                while isValid2 == False:
                    print("How do you want the customer record sorted by?")
                    print("1: Customer number")
                    print("2: Customer phone")
                    print("3: Art preference")
                    choice2 = input()

                    if int(choice2) == 1:
                        isValid2 = True
                        print("Sorting customer record by number.")
                        querySort = "select * from CUSTOMER order by CustNumber"
                    elif int(choice2) == 2:
                        isValid2 = True
                        print("Sorting customer record by phone.")
                        querySort = "select * from CUSTOMER order by CustPhone"
                    elif int(choice2) == 3:
                        isValid2 = True
                        print("Sorting customer record by preference.")
                        querySort = "select * from CUSTOMER order by ArtPref"
                    else:
                        print("Invalid choice. Please re-enter.")
                        
                    newCursor.execute(querySort)
                    thisRecord = newCursor.fetchall()
                    for row in thisRecord:
                        print("Number: ", row[0])
                        print("Phone: ", row[1])
                        print("Art Preference: ", row[2], "\n")
                        
            elif int(choice) == 4:
                isValid = True
                while isValid2 == False:
                    print("How do you want the art show record sorted by?")
                    print("1: Artist name")
                    print("2: Date and time")
                    print("3: Location")
                    print("4: Contact name")
                    print("5: Contact phone")
                    choice2 = input()

                    if int(choice2) == 1:
                        isValid2 = True
                        print("Sorting art show record by artist name.")
                        querySort = "select * from ART_SHOW order by ArtistName"
                    elif int(choice2) == 2:
                        isValid2 = True
                        print("Sorting art show record by date and time.")
                        querySort = "select * from ART_SHOW order by Date_and_Time"
                    elif int(choice2) == 3:
                        isValid2 = True
                        print("Sorting art show record by location.")
                        querySort = "select * from ART_SHOW order by Location"
                    elif int(choice2) == 4:
                        isValid2 = True
                        print("Sorting art show record by contact name.")
                        querySort = "select * from ART_SHOW order by ContactName"
                    elif int(choice2) == 5:
                        isValid2 = True
                        print("Sorting art show record by contact phone.")
                        querySort = "select * from ART_SHOW order by ContactPhone"
                    else:
                        print("Invalid choice. Please re-enter.")
                        
                    newCursor.execute(querySort)
                    thisRecord = newCursor.fetchall()
                    for row in thisRecord:
                        print("Artist: ", row[0])
                        print("Date & Time: ", row[1])
                        print("Location: ", row[2])
                        print("Contact Name: ", row[3])
                        print("Contact Phone: ", row[4], "\n")
                        
            else:
                print("Invalid choice. Please re-enter.")

        # Part 3: Ask the user to choose which record to search for.
        isValid = False
        isValid2 = False
        while isValid == False:
            print("Select which record to search into.")
            print("1: Artist")
            print("2: Artwork")
            choice = input()

            if int(choice) == 1:
                isValid = True
                while isValid2 == False:
                    print("What to search for in the artist record?")
                    print("1: Search for artists age 20-39")
                    print("2: Search for artists age 40-59")
                    print("3: Search for artists age 60-79")
                    print("4: Search for artists age 80+")
                    choice2 = input()

                    if int(choice2) == 1:
                        isValid2 = True
                        querySearch = "select * from ARTIST where artistAge >= 20 AND artistAge < 40"
                    elif int(choice2) == 2:
                        isValid2 = True
                        querySearch = "select * from ARTIST where artistAge >= 40 AND artistAge < 60"
                    elif int(choice2) == 3:
                        isValid2 = True
                        querySearch = "select * from ARTIST where artistAge >= 60 AND artistAge < 80"
                    elif int(choice2) == 4:
                        isValid2 = True
                        querySearch = "select * from ARTIST where artistAge >= 80"
                    else:
                        print("Invalid choice. Please re-enter.")

                    newCursor.execute(querySearch)
                    thisRecord = newCursor.fetchall()
                    print("\nNow printing artist record")
                    for row in thisRecord:
                        print("Name: ", row[0])
                        print("Phone: ", row[1])
                        print("Address: ", row[2])
                        print("Birthplace: ", row[3])
                        print("Age: ", row[4])
                        print("Art Style: ", row[5], "\n")    
            elif int(choice) == 2:
                isValid = True
                while isValid2 == False:
                    print("What to search for in the artwork record?")
                    print("1: Artwork with price up to 1000")
                    print("2: Artwork with price greater than 1000 and up to 2000")
                    print("3: Artwork with price greater than 2000 and up to 3000")
                    print("4: Artwork with price greater than 3000 and up to 4000")
                    print("5: Artwork with price greater than 4000 and up to 5000")
                    choice2 = input()
                    
                    if int(choice2) == 1:
                        isValid2 = True
                        querySearch = "select * from ART_WORK where Price <= 1000"
                    elif int(choice2) == 2:
                        isValid2 = True
                        querySearch = "select * from ART_WORK where Price > 1000 AND Price <= 2000"
                    elif int(choice2) == 3:
                        isValid2 = True
                        querySearch = "select * from ART_WORK where Price > 2000 AND Price <= 3000"
                    elif int(choice2) == 4:
                        isValid2 = True
                        querySearch = "select * from ART_WORK where Price > 3000 AND Price <= 4000"
                    elif int(choice2) == 5:
                        isValid2 = True
                        querySearch = "select * from ART_WORK where Price > 4000 AND Price <= 5000"
                    else:
                        print("Invalid choice. Please re-enter.")

                    newCursor.execute(querySearch)
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
            else:
                print("Invalid choice. Please re-enter.")
            
# If something unexpected occured, display the error message and explain why.
except Error as e:
    print("An exception has occured", e)

# Regardless of the outcome above, be sure to close connection afterwards.
finally:
    if (newConnect.is_connected()):
        newCursor.close()
        newConnect.close()
        print("MySQL connection is closed")
        
