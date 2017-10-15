# general imports
from nba_py import team
from os.path import join
import json
import nba_simulator.Constants as Constants


# helper functions
def create_game_logs_file(team_id):
    """
    Creates file for each NBA team containing game info from last season

    :param team_id: ID number of the team
    """
    path = join(Constants.TEAM_BASE_PATH, Constants.TEAM_DICT[team_id] + '.json')
    game_logs = team.TeamGameLogs(team_id, '2016-17').json
    with open(path, 'w') as outfile:
        json.dump(game_logs, outfile)


def init():
    """
    Loop through every single team ID and create a file
    """
    for team_id in Constants.TEAM_DICT.keys():
        create_game_logs_file(team_id)

init()
