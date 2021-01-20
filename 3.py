import csv
import sqlite3

conn=sqlite3.connect("basadannih.db")
cursor=conn.cursor()

cursor.execute("""CREATE TABLE Predpriyatie (name text, okna integer, vremya integer, raboti integer, tovari integer) """)
Predpriyatie = [('Pered Avtomatization', '8','5','60','81'),('Posle Avtmzn','12','8','97','169')]
cursor.executemany("INSERT INTO Predpriyatie VALUES (?,?,?,?,?)", Predpriyatie)

sqlupdate="""
UPDATE Predpriyatie
SET okna = '10', vremya = '6', raboti = '89', tovari = '149' 
WHERE name = 'Posle Avtmzn'

cursor.execute(sqlupdate)
conn.commit()
