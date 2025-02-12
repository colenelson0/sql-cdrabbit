# Use this file to create/reset the CDrabbit database back to its default state

import sqlite3

con = sqlite3.connect("cdrabbit.db")

# Runs the initial code that creates the tables and adds the data
with open('cdrabbit.sql') as f:
    con.executescript(f.read())

con.close()

print("The database has been created/reset.")