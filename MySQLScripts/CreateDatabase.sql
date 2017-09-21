Create DATABASE IF NOT EXISTS PairingsBot;

GRANT USAGE ON *.* TO PairingsBotMod@localhost IDENTIFIED BY 'password'; --Change this later, especially for production
GRANT ALL PRIVILEGES ON PairingsBot.* TO PairingsBotMod@localhost;
FLUSH PRIVILEGES;

CREATE TABLE IF NOT EXISTS PairingsBot.Player (PlayerId INT NOT NULL AUTO_INCREMENT,
                                               TwitchName Varchar(25),
                                               LichessName Varchar(25),
                                               Rating INT,
                                               PRIMARY KEY (PlayerId)
                                              );
