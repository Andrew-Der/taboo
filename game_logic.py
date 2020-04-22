import json
from json import JSONEncoder

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
        self.forceQuit        = False
        self.teamAPlayerIds   = []
        self.teamBPlayerIds   = []


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

    if not GAME_DB[game_id]: 
        gh = GameHandle(game_id)    

    # create dummy Player 
    name = "Andrew"
    isTeamA = False
    player = Player(name, isTeamA, game_id)

    try:
        add_player_to_gh(gh, player)
    except NameError as err:
        print("Player already exists, use a diff name")
        return False

    # write gh to db
    GAME_DB[game_id] = gh
    return True


# the gameHandle exists
# the array of players exist
# need to retrieve the game handle and change some variables and write it out
def start_game (request):
    import pdb; pdb.set_trace()
    print("Starting Game")
    #get the game
    return