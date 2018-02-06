CREATE TABLE IF NOT EXISTS pairingsbotdb.Player (PlayerId INT NOT NULL AUTO_INCREMENT,
                                               TwitchName Varchar(25),
                                               LichessName Varchar(25),
                                               Rating INT,
                                               PRIMARY KEY (PlayerId)
                                              );

CREATE TABLE IF NOT EXISTS pairingsbotdb.Tournament (TournamentId INT NOT NULL AUTO_INCREMENT,
                                                    Name Varchar(25),
                                                    NumberOfRounds INT,
                                                    StartDate INT,
                                                    RoundLength INT,
                                                    PRIMARY KEY (TournamentId)
                                                    );
