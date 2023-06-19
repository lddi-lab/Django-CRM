# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip instal mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Qw3rty812!',
)

# prepare a cursor objext
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE eldirco")

print("All Done!")