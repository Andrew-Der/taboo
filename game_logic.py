import json
from json import JSONEncoder

from helpers import add_player_to_gh

class Card:
    def __init__(self):
        self.id   = 0
        self.word = ""
        self.taboo_words = ""

class Player:
    def __init__(self, name, isTeamA, gameId):
        self.name    = name
        self.isTeamA = isTeamA
        self.gameId        = gameId
        self.cardsGotRight = 0
        self.cardsGotWrong = 0

class GameHandle:
    def __init__(self, gameId):
        self.id = gameId 
        self.usedCardIds = []
        self.teamAScore = 0
        self.teamBScore = 0
        self.gameStarted  = False
        self.roundStarted = False
        # self.timer
        self.activePlayerId   = 0
        self.watchingPlayerId = 0
        self.gameOver         = False
        self.roundsCompleted  = 0
        self.teamAPlayerIds   = []
        self.teamBPlayerIds   = []

    def __str__(self):
        print("id : " + self.id)
        print(f"gameStarted : ${self.gameStarted}")
        print(f"teamAPlayerIds : ${self.teamAPlayerIds}")
        print(f"teamBPlayerIds : ${self.teamBPlayerIds}")
        return ""
class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__


game_handle_db = "games.json"
player_db = "players.json"

GAME_DB = {}

""" Initializes a game with a player. 
    Every player should call this method 
    Returns: Bool if successfully init game """
def init_game(server):

    game_id = server.path
    gh = GAME_DB.get(game_id)

    if not gh: 
        gh = GameHandle(game_id)    

    # create dummy Player 
    name = "Andrew"
    isTeamA = False
    player = Player(name, isTeamA, game_id)

    try:
        add_player_to_gh(gh, player)
    except Exception as err:
        print(err)
        return False

    # write gh to db
    GAME_DB[game_id] = gh

    print("Game DB")
    print(GAME_DB[game_id])

    return True


# the gameHandle exists
# the array of players exist
# need to retrieve the game handle and change some variables and write it out
def start_game(server):
    
    game_id = server.path
    gh = GAME_DB.get(game_id)

    if not gh:
        raise Exception("Game id not found in db")

    if gh.gameStarted:
        raise Exception("Game already started, please use a new url")

    if gh.gameOver:
        raise Exception("Game already ended, please use a new url")

    if len(gh.teamAPlayerIds) < 1 or len(gh.teamBPlayerIds) < 1:
        raise Exception("Each team must have more than zero players")

    gh.gameStarted = True
    gh.activePlayer = gh.teamAPlayerIds[0]
    gh.watchingPlayer = gh.teamBPlayerIds[0]

    return