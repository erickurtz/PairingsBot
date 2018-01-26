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

