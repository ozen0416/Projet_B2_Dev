USE Battleship;

-- Delete tables if they already exist
DROP TABLE IF EXISTS GamePlayer;
DROP TABLE IF EXISTS Turn;
DROP TABLE IF EXISTS ShipCell;
DROP TABLE IF EXISTS Game;
DROP TABLE IF EXISTS Player;

CREATE TABLE Player(
  id_player INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL
);

CREATE TABLE Game(
  id_game INT AUTO_INCREMENT PRIMARY KEY,
  id_p1 INT,
  id_p2 INT,
  id_winner INT,
  started DATETIME NOT NULL,
  ended DATETIME,
  FOREIGN KEY(id_p1) REFERENCES Player(id_player),
  FOREIGN KEY(id_p2) REFERENCES Player(id_player),
  FOREIGN KEY(id_winner) REFERENCES Player(id_player)
);

CREATE TABLE GamePlayer(
  id_game INT,
  id_player INT,
  PRIMARY KEY(id_game, id_player),
  FOREIGN KEY(id_game) REFERENCES Game(id_game) ON DELETE CASCADE,
  FOREIGN KEY(id_player) REFERENCES Player(id_player) ON DELETE CASCADE
);

CREATE TABLE Turn(
  id_turn INT AUTO_INCREMENT PRIMARY KEY,
  id_game INT,
  id_player INT,
  turn_count INT,
  x INT,
  y INT,
  status VARCHAR(50),
  FOREIGN KEY(id_game) REFERENCES Game(id_game) ON DELETE CASCADE,
  FOREIGN KEY(id_player) REFERENCES Player(id_player)
);

CREATE TABLE ShipCell(
  id_cell INT AUTO_INCREMENT PRIMARY KEY,
  id_player INT,
  id_game INT,
  x INT,
  y INT,
  FOREIGN KEY(id_game) REFERENCES Game(id_game) ON DELETE CASCADE,
  FOREIGN KEY(id_player) REFERENCES Player(id_player)
);
