#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 20:26:46 2022

@author: sumitbhiungade
"""

import sqlite3

#connection to the database
connection = sqlite3.connect('movies_database.db')

#cursor for the connection
cursor = connection.cursor()

#create movie_db table
command1= """CREATE TABLE IF NOT EXISTS movie_db(
                movie_name text,
                actor_name text,
                actress_name text,
                director text,
                year_of_release integer)"""

#execute the above command
cursor.execute(command1)

#inserting records in the database
cursor.execute("INSERT INTO movie_db VALUES ('Avatar','Sam','Kate','James Camron', 2009)")
cursor.execute("INSERT INTO movie_db VALUES ('Tiatanic','Leo','Kate','James', 1997)")
cursor.execute("INSERT INTO movie_db VALUES ('Gravity','George','Sandra','Alfonso Cuarón', 2013)")
cursor.execute("INSERT INTO movie_db VALUES ('The Nun','Jonas','Vera','Corin Hardy', 2018)")

#Quering into the database and getting results

cursor.execute("SELECT * FROM movie_db")
cursor.execute("SELECT movie_name FROM movie_db WHERE actor_name = 'Sam'")
cursor.execute("SELECT movie_name FROM movie_db WHERE actress_name = 'Vera'")




#printing the results
results = cursor.fetchall()
print(results)




























