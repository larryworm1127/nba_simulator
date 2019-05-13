"""
This module retrieves team game log data (regular season and playoff) and team
season data, and store the data inside a JSON file
"""

# general imports
import json
import os.path

from nba_py import team, constants

from constant import TEAM_BASE_PATH
from constant import TEAM_PLAYOFF_PATH
from constant import TEAM_SEASON_PATH
from constant import TEAM_DICT


# helper functions
def create_game_logs_file(team_id):
    """Creates file for each NBA team containing game info from last season

    :param team_id: ID number of the team
    """
    # team game log
    path = os.path.join(TEAM_BASE_PATH, TEAM_DICT[team_id] + '.json')
    if not os.path.exists(path):
        print("Retrieving team " + TEAM_DICT[team_id] +
              " game log, season stats ... Please wait.")
        game_logs = team.TeamGameLogs(team_id, '2016-17').json
        with open(path, 'w') as outfile:
            json.dump(game_logs, outfile)

    # playoff game log
    playoff_path = os.path.join(TEAM_PLAYOFF_PATH, TEAM_DICT[team_id] + '.json')
    if not os.path.exists(playoff_path):
        playoff_games = team.TeamGameLogs(team_id, '2016-17',
                                          constants.SeasonType.Playoffs).json
        if len(playoff_games['resultSets'][0]['rowSet']):
            with open(playoff_path, 'w') as playoff_files:
                json.dump(playoff_games, playoff_files)

    # season stats
    season_path = os.path.join(TEAM_SEASON_PATH, TEAM_DICT[team_id] + '.json')
    if not os.path.exists(season_path):
        season_stats = team.TeamSeasons(team_id).json
        with open(season_path, 'w') as season_files:
            json.dump(season_stats, season_files)


def init():
    """Loop through every single team ID and create a file
    """
    for team_id in TEAM_DICT.keys():
        create_game_logs_file(team_id)
