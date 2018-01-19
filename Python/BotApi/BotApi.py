#!/usr/bin/python3

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
    print("\n1. Insert into database.")
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

# This is a guess the number game.

# import random

# guessesTaken = 0
# print('Hello! What is your name?')

# myName = input()
# number = random.randint(1, 20)

# print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

# while guessesTaken < 6:
    # print('Take a guess.') # There are four spaces in front of print.
    # guess = input()
    # guess = int(guess)
    # guessesTaken = guessesTaken + 1

    # if guess < number:
        # print('Your guess is too low.') # There are eight spaces in front of print.

    # if guess > number:
        # print('Your guess is too high.')

    # if guess == number:
        # break

# if guess == number:
    # guessesTaken = str(guessesTaken)
    # print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

# if guess != number:
    # number = str(number)

#     print('Nope. The number I was thinking of was ' + number)
