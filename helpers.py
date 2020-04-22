
import json

from game_logic import game_handle_db

def game_exists_in_db(game_id):

    exists = False
    try: 
        with open(game_handle_db, "r") as read_file:
            game_handles = json.load(read_file)
            if isinstance(game_handles, list):
                exists = any([gh["id"] == game_id for gh in game_handles])
            else:
                raise TypeError

    except TypeError:
        print("GameHandles in file are not type List")

    return exists


def write_gh_to_db(gh):


    with open(game_handle_db, "r") as read_file:
        game_handles = json.load(read_file)

        for idx, game in enumerate(game_handles):
            if game["id"] == gh.id:
                game_handles[idx]["id"] = gh.id 
                game_teamAScore = gh.teamAScore
    print("asd")
    import pdb; pdb.set_trace()


""" Add PLayer to the GH in appropiate team """
def add_player_to_gh(gh, player):

    player_exists = False
    if player.isTeamA:
        if player.name in gh.teamAPlayerIds:
            player_exists = True
        else:
            gh.teamAPlayerIds.append(player.name)
    else:
        if player.name in gh.teamBPlayerIds:
            player_exists = True
        else:
            gh.teamBPlayerIds.append(player.name)

    if player_exists:
        raise NameError("Player already exists")

