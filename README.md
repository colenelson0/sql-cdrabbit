# Overview

This program allows a user to interact with a database which contains CDs and artists for those CDs. In order to get started, the user must first create the database by running the 'create-db.py' file, which by default contains 15 artists and 20 CDs.
The program offers seven options for action: The first three options allow the user to view the CDs that are in stock, the list of CDs in the database, and the list of artists in the database. The next two options allow the user to add copies of CDs to the inventory and report new sales for the CDs. The last two options allow the user to add their own artists and CDs to the database.

The reason that I decided to make this program with these tools is to show how useful and easy to use SQL databases are, as well as how fun they can be. Python and sqlite3 have been great tools for learning how the front end and back end interact in a software environment.

[CD Database Program in Python](https://www.youtube.com/watch?v=9l9gGHLWSWA)

# Relational Database

The database contains data for CDs in a CD store (a store called CDrabbit, specifically), as well the artists and bands attributed to those CDs.

The table for CDs, called cd, contains a primary key, a title for the CD, the foreign key for the artist, the genre of the CD, the release year of the CD, the number of copies currently in stock, and the number of sales for the CD. The table for the artists and bands, called artist, contains a primary key, a name for the artist/band, and the type, which is whether it is a solo artist, a group/band, or not specified to be either.

# Development Environment

The main program for the project was developed using Visual Studio Code for Mac, since it tends to work well with Python programs. The sql file was initially developed using MySQL Workbench, but due to the differences between MySQL and sqlite, it was mostly rewritten using VS Code.

The programs for this project were developed using Python and the sqlite3 library.

# Useful Websites

- [Python sqlite3 Tutorial](https://docs.python.org/3/library/sqlite3.html#tutorial)
- [How To Use One-to-Many Database Relationships with SQLite](https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-and-sqlite)
- [SQLite SELECT](https://www.sqlite.org/lang_select.html)
- [Python String Methods](https://www.w3schools.com/python/python_ref_string.asp)
- [SQL UPDATE Statement](https://www.w3schools.com/sql/sql_update.asp)

# Future Work

- Allow the user to select the artist they want to attribute to a CD if there are more than one with the same name
- Add more practical use to the artist_type column in the artist table
