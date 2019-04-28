"""
description:
Script to create a database for the database practical for advanced programming.
date: 19/02/28
@author: ksuchak
"""
# Imports
import sqlite3 as sql3

with sql3.connect('results_db.sqlite') as con:
    c = con.cursor()
    # create a table and insert an entry
    c.execute("CREATE TABLE Results (address text, burglaries integer)")
    c.execute("INSERT INTO Results VALUES ('Queen Vic', 2)")
    con.commit()
