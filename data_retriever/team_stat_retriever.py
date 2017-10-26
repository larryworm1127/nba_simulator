# general imports
import json
from os.path import join
from data_retriever import Main
from nba_py import team
from data_retriever import file_check

# create preliminary files for teams
file_check.init()
with open(Main.TEAM_DICT_PATH, 'r') as team_dict_file:
    team_dict = json.load(team_dict_file)


# helper functions
def create_game_logs_file(team_id):
    """
    Creates file for each NBA team containing game info from last season

    :param team_id: ID number of the team
    """
    path = join(Main.TEAM_BASE_PATH, team_dict[team_id] + '.json')
    game_logs = team.TeamGameLogs(team_id, '2016-17').json
    with open(path, 'w') as outfile:
        json.dump(game_logs, outfile)


def init():
    """
    Loop through every single team ID and create a file
    """
    for team_id in team_dict.keys():
        create_game_logs_file(team_id)

init()
