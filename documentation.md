
# Documentation

1. **Game**
2. **Matchmaking**
3. **Client**
4. **Server**
5. **UI/UX**
6. **BDD**


# 1.  Game
### Typical game
Game is turn-based
Each player has to place his pieces onto his side of the map
Once ships are placed, each player will have to choose a cell from its opponent grid.
Either if a ship is touched or not, the player is noticed
When a ship is sunk, the player is also noticed
One player wins when every ship on its opponent side has been sunk


# 3. Server
The server will receive socket information containing both a header for server-side interpretation for the data and the actual data.

A handler will have to give the data to the `Game` instance

Example of data to be sent (clients would have to send its list of ships, or a target hit)
```py
ship_cells = [{"_pos": {"_x": 0, "_y": 1}}, {"_pos": {"_x": 0, "_y": 1}}, {"_pos": {"_x": 0, "_y": 1}}]

data = {"_ships": [{"_size": 3, "_pos": {"_x": 0, "_y": 1,},  "_ship_cells": ship_cells}]}
```

A request **MUST** contain the type of the request and its sub-request, otherwise it will be discarded.
```json
{
	"request": ["GAME", "HIT"],
	"client_id": 12,
	"game_id": 34,
	"data": {"_x": 1, "_y": 0}
}
```

#### Requests:
- `GAME` this will inform the server your request is about an in-progress game.
- `MATCHMAKING` this will inform the server your request is about the pregame matchmaking system.

#### Sub-requests:
- `HIT` to inform the server that you want to try a hit at (`x`,`y`)
- `QUEUE_IN` to inform the server that you are willing to join the matchmaking queue
- `QUEUE_OUT` to inform the server that you are willing to leave the matchmaking queue
- `MESSAGE` to send a message to the other client

This is best explained in the `Class Hierarchy` page

`WholeGameData`: The whole data that happened during the game, each turn is recorded and store from the beginning to the end of the game in the server.

### /!\ Important point
How are we going to handle a disconnected client when an opponent make a turn?

##### Possible solution
When in a `pair`, one of the clients has lost connection to the server and is willing to reconnect to the game, the client will have to notice this event to the application to be prepared of receiving the `WholeGameData`.
That will allow us to recreate the game at the point it actually is, even for turns that could be made after the `client` was disconnected.

Server-side, it shall scan for whether new incoming socket connection was previously linked to another `client` as a `pair`. If so, we set to this `client` inside of the `pair` the previous disconnected one and send after the pairing the `WholeGameData` to this client.

As for now, this is yet not implemented. If a client connection is closed the game will just be frozen to its state.

#### What is a `Pair` to the server?
A `pair` is a set of two clients connections, that are currently linked by the server for post-matchmaking communication (either messaging or game-related events):

- The current `Game` instance to process the game and keep a track of its different states.
- An `id` that will be the game id
- A First `Client`
- A Second `Client`


### Bad data
Bad data can happen as sockets could not send or receive properly the transmitted data.
But there could be few cases in which a user would try breaking the behavior of the game and send data when it is not his turn, simulating an opponent attack

To prevent that, we could possibly make an end and cancel any game receiving that kind of suspicious sent packets from one of its clients.
We also could simply discard any data sent from clients attempting a request to a game they do not belong in.

An ideal approach would be to blacklist every IP trying to perform too much illegal requests in a span of time, but it could also be some huge amount of work to get it as intended.


