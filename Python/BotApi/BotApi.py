#!/usr/bin/python3

# Will use curses for the GUI

import pymysql

def getConnection():

     connection = pymysql.connect(host='pairingsbot_db_1',
                                 user='root',
                                 password='root',
                                 db='pairingsbotdb',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
     return connection

def testDatabase():
    try:
        connection = getConnection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO Player (TwitchName, LichessName, Rating) Values (%s, %s, %s)"
            cursor.execute(sql, ('test', 'test', 1500))

            connection.commit()
    finally:
        connection.close()

def readDatabase():
    print("Reading the database")
    try:
        connection = getConnection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Player"
            cursor.execute(sql)
            for twitchName in cursor:
                print(twitchName)
    finally:
        connection.close()

def initialize():
    print("Hello!")
    print("\nWhat would you like to do?")
    print("\n1. Add player.")
    print("\n2. Read database.")
    print("\n3. Exit.")
    number = input()
    while number != "3":
        if number == "1":
            testDatabase()
        elif number == "2":
            readDatabase()
        else:
            print("Try again.")

        print("\nWhat would you like to do?")
        print("\n1. Insert into database.")
        print("\n2. Read database.")
        print("\n3. Exit.")
        number = input()

initialize()
