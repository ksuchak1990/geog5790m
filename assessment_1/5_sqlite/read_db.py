"""
description:
A script to read the database for the database practicals for advanced
programming.
date: 19/02/28
@author: ksuchak
"""
# Imports
import sqlite3 as sql3

with sql3.connect('results_db.sqlite') as con:
    c = con.cursor()
    # print out each row ordered by burglaries
    for row in c.execute("SELECT * FROM Results ORDER BY burglaries"):
        print("{0}\t{1}".format(row[0], row[1]))
