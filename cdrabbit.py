# Main program
# DO NOT run this program without running create-db.py at least once beforehand

import sqlite3

con = sqlite3.connect("cdrabbit.db")
cur = con.cursor()

# Saves the current number of CDs in the database
for row in cur.execute("SELECT COUNT(*) FROM cd"):
    rowCount = row[0]

def display_menu():
    print("\nDISPLAY DATA:\nIf you would like to see which CDs are in stock, enter 1")
    print("If you would like to see all the CDs in the database, enter 2")
    print("If you would like to see all the artists in the database, enter 3")
    print("UPDATE DATA:\nIf you would like to add copies to the stock of a CD, enter 4")
    print("If you would like to report new sales for a CD, enter 5")
    print("INSERT DATA:\nIf you would like to add a new artist/band to the database, enter 6")
    print("If you would like to add a new CD to the database, enter 7")
    print("If you would like to exit the program, enter 0")
    print("\nENTER: ")

print("Hello, and welcome to the CDrabbit database program.")
display_menu()
properInput = False
while not properInput:
    try:
        selection = int(input())
        if selection < 0 or selection > 7:
            print("Invalid - out of range")
            print("ENTER: ")
        else:
            properInput = True
    except ValueError:
        print("Invalid - not an integer")
        print("ENTER: ")
while selection != 0:
    # MENU SELECTION 1
    if selection == 1:
        # CDs in stock
        print("\nEnter the number for one of the following statements:")
        print("\n1 - Show me the top selling CDs")
        print("2 - Show me the most recently released CDs")
        print("3 - Show me all the CDs from a certain genre")
        print("4 - Show me all the CDs from a certain artist/band")
        print("\nENTER: ")
        selection = int(input())
        if selection == 1:
            print("\nTop selling CDs:")
            i = 1
            for row in cur.execute("SELECT title, rel_year, artist_name, sales FROM cd JOIN artist a \
                            ON cd.artist_id = a.artist_id WHERE in_stock > 0 ORDER BY sales DESC LIMIT 10"):
                text = "{0:>2}. {1} ({2}), by {3} [{4} sales]"
                print(text.format(i, row[0], row[1], row[2], row[3]))
                i += 1
        elif selection == 2:
            print("\nMost recent CDs:")
            i = 1
            for row in cur.execute("SELECT title, rel_year, artist_name, in_stock FROM cd JOIN artist a \
                            ON cd.artist_id = a.artist_id WHERE in_stock > 0 ORDER BY rel_year DESC LIMIT 5"):
                text = "{0:>2}. {1} ({2}), by {3} [{4} in stock]"
                print(text.format(i, row[0], row[1], row[2], row[3]))
                i += 1
        elif selection == 3:
            print("\nThe genres currently in stock are:")
            for row in cur.execute("SELECT DISTINCT genre FROM cd WHERE in_stock > 0 ORDER BY genre"):
                print("- " + row[0])
            print("Which would you like to search for?")
            selection = input().lower()
            params = (selection,)
            print("\n" + selection.capitalize() + " CDs:")
            i = 1
            for row in cur.execute("SELECT title, rel_year, artist_name, in_stock FROM cd JOIN artist a \
                            ON cd.artist_id = a.artist_id WHERE in_stock > 0 AND genre = ? ORDER BY artist_name", params):
                text = "{0:>2}. {1} ({2}), by {3} [{4} in stock]"
                print(text.format(i, row[0], row[1], row[2], row[3]))
                i += 1
        elif selection == 4:
            print("\nWho would you like to search for?")
            selection = input()
            params = (selection,)
            print("\nCDs by " + selection + ":")
            i = 1
            for row in cur.execute("SELECT title, rel_year, in_stock FROM cd JOIN artist a \
                            ON cd.artist_id = a.artist_id WHERE in_stock > 0 AND artist_name = ? ORDER BY title", params):
                text = "{0:>2}. {1} ({2}) [{3} in stock]"
                print(text.format(i, row[0], row[1], row[2]))
                i += 1
    
    # MENU SELECTION 2
    elif selection == 2:
        # Display CDs in the database
        print("\nThe following CDs are currently in the database:")
        i = 1
        for row in cur.execute("SELECT title, artist_name, in_stock FROM cd JOIN artist a \
                            ON cd.artist_id = a.artist_id"):
                text = "{0:>2}. {1}, by {2} [{3} in stock]"
                print(text.format(i, row[0], row[1], row[2]))
                i += 1

    # MENU SELECTION 3
    elif selection == 3:
        # Display artists in the database
        print("\nThe following artists are currently in the database:")
        i = 1
        for row in cur.execute("SELECT artist_name, artist_type FROM artist"):
                text = "{0:>2}. {1} [{2}]"
                print(text.format(i, row[0], row[1]))
                i += 1
    
    # MENU SELECTION 4
    elif selection == 4:
        # Add to the stock of a CD
        print("\nWhat is the key/number of the CD you want to add to?")
        print("[If you don't know, go back by entering any negative integer]")
        print("\nENTER: ")
        properInput = False
        while not properInput:
            try:
                selection = int(input())
                if selection > rowCount or selection == 0:
                    print("Invalid - out of range")
                    print("ENTER: ")
                else:
                    properInput = True
            except ValueError:
                print("Invalid - not an integer")
                print("ENTER: ")
        
        if selection > 0:
            # A key has been selected
            # Determine the number of copies to add
            print("\nHow many copies should be added?")
            print("ENTER: ")
            properInput = False
            while not properInput:
                newCopies = int(input())
                if newCopies < 1:
                    print("Invalid - cannot be less than 1")
                    print("ENTER: ")
                else:
                    properInput = True
            
            # First the current number must be retreived from the database
            params = (selection,)
            for row in cur.execute("SELECT in_stock FROM cd WHERE cd_id= ?", params):
                currentCopies = row[0]
            # Then the total number is calculated and added to the params
            params = (currentCopies + newCopies, selection,)
            # Then the value is updated in the database
            cur.execute("UPDATE cd SET in_stock= ? WHERE cd_id= ?", params)
            con.commit()
            # A verification message is printed
            text = "{0} copies have been added to the stock"
            print(text.format(newCopies))
    
    # MENU SELECTION 5
    elif selection == 5:
        # Add to the sales of a CD
        print("\nWhat is the key/number of the CD you want to add to?")
        print("[If you don't know, go back by entering any negative integer]")
        print("\nENTER: ")
        properInput = False
        while not properInput:
            try:
                selection = int(input())
                if selection > rowCount or selection == 0:
                    print("Invalid - out of range")
                    print("ENTER: ")
                else:
                    properInput = True
            except ValueError:
                print("Invalid - not an integer")
                print("ENTER: ")
        
        if selection > 0:
            # A key has been selected
            # Determine the number of sales to add
            print("\nHow many sales should be added?")
            print("ENTER: ")
            properInput = False
            while not properInput:
                newSales = int(input())
                if newSales < 1:
                    print("Invalid - cannot be less than 1")
                    print("ENTER: ")
                else:
                    properInput = True
            
            # First the current number must be retreived from the database
            params = (selection,)
            for row in cur.execute("SELECT sales FROM cd WHERE cd_id= ?", params):
                currentSales = row[0]
            # Then the total number is calculated and added to the params
            params = (currentSales + newSales, selection,)
            # Then the value is updated in the database
            cur.execute("UPDATE cd SET sales= ? WHERE cd_id= ?", params)
            con.commit()
            # A verification message is printed
            text = "{0} CD sales have been added to the database"
            print(text.format(newSales))

    # MENU SELECTION 6
    elif selection == 6:
        # Add an artist/band to the database
        # Get the number of artists in the database
        for row in cur.execute("SELECT COUNT(*) FROM artist"):
            artistCount = row[0]

        # Get value for artist_type column
        print("\nIs this new entry a solo artist (not a band/group)?")
        selection = input().lower()
        if selection == "yes":
            artistType = "solo";
            language = "artist";
        elif selection == "no":
            artistType = "group";
            language = "band";
        else:
            artistType = "unspecified";
            language = "artist/band";
    
        # Get value for artist_name column
        text = "What is the name of the {0}?"
        print(text.format(language))
        artistName = input()

        # Insert the artist into the database
        params = (artistCount + 1, artistName, artistType,)
        cur.execute("INSERT INTO artist VALUES (?, ?, ?)", params)
        con.commit()
        # A verification message is printed
        text = "\n{0} has been added to the database"
        print(text.format(artistName))

    # MENU SELECTION 7
    elif selection == 7:
        # Add a CD to the database
        print("\nWhat is the artist/band for the CD?")
        artistName = input()

        # Check for the existence of this artist in the database
        params = (artistName,)
        for row in cur.execute("SELECT COUNT(*) FROM artist WHERE artist_name= ?", params):
            matchCount = row[0]
        if matchCount == 0:
            # There are no matches for the artist
            print("Invalid - artist must be in database")
            print("Add the artist/band to the database and try again")
        else:
            # There is at least one match for the artist
            if matchCount > 1:
                print("Multiple matches found; first in database will be used")
            # Retrieve the first key that matches the name
            keyList = []
            for row in cur.execute("SELECT artist_id FROM artist WHERE artist_name= ?", params):
                keyList.append(row[0])
            
            # Get value for title column
            print("What is the title of the CD?")
            cdTitle = input()

            # Get value for genre column
            print("What is the genre of the CD?")
            cdGenre = input().lower()

            # Get value for year column
            print("What is the release year of the CD?")
            properInput = False
            while not properInput:
                try:
                    cdYear = int(input())
                    properInput = True
                except ValueError:
                    print("Invalid - not an integer")

            # Remaining two columns will be set to 0
            # Insert the CD into the database
            rowCount += 1
            params = (rowCount, cdTitle, keyList[0], cdGenre, cdYear,)
            cur.execute("INSERT INTO cd VALUES (?, ?, ?, ?, ?, 0, 0)", params)
            con.commit()
            # A verification message is printed
            text = "\n{0} by {1} has been added to the database"
            print(text.format(cdTitle, artistName))

    # Get next menu selection from user
    print("\n-----------------------------------------------------------------")
    display_menu()
    properInput = False
    while not properInput:
        try:
            selection = int(input())
            if selection < 0 or selection > 7:
                print("Invalid - out of range")
                print("ENTER: ")
            else:
                properInput = True
        except ValueError:
            print("Invalid - not an integer")
            print("ENTER: ")