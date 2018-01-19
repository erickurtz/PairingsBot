#!/usr/bin/python3

import pymysql

connection = pymysql.connect(host='localhost',
                             user='PairingsBotMod',
                             password='password',
                             db='PairingsBot',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def testDatabase():
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO Player (TwitchName, LichessName, Rating) Values (%s, %s, %s)"
            cursor.execute(sql, ('test', 'test', 1500))

            connection.commit()
    finally:
        connection.close()

def readDatabase():
    print("Reading the database")
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Player"
            cursor.execute(sql)
            for twitchName in cursor:
                print twitchName
    finally:
        connection.close()

readDatabase()
# import mysql.connector as mariadb

# mariadb_connection = mariadb.connect(user='PairingsBotMod', password='password', database='PairingsBot')
# cursor = mariadb_connection.cursor()

# #retrieving information
# some_name = 'Georgi'
# cursor.execute("SELECT first_name,last_name FROM employees WHERE first_name=%s", (some_name,))

# for first_name, last_name in cursor:
    # print("First name: {}, Last name: {}").format(first_name,last_name)

# #insert information
# try:
    # cursor.execute("INSERT INTO employees (first_name,last_name) VALUES (%s,%s)", ('Maria','DB'))
# except mariadb.Error as error:
    # print("Error: {}".format(error))

# mariadb_connection.commit()
# print "The last inserted id was: ", cursor.lastrowid

# mariadb_connection.close()
