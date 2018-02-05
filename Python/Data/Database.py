import pymysql

connection = pymysql.connect(host='pairingsbot_db_1',
                             user='root',
                             password='root',
                             db='pairingsbotdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def save_pairing_model(pairing_model):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO Tournament ('Name', 'NumberOfRounds', 'RoundDuration', 'StartDate')"
            cursor.execute(sql, 
                    (pairing_model.tournament_name,
                    pairing_model.number_of_rounds, 
                    pairing_model.start_date,
                    pairing_model.round_duration))
    finally:
        connection.close()


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
                print(twitchName)
    finally:
        connection.close()

