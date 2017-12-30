"""
This module retrieves team game log data (regular season and playoff) and team season data, and store
the data inside a JSON file
"""

# general imports
from json import dump, load
from os.path import join, exists
from data_retriever import Main
from nba_py import team, constants
from data_retriever import create_other_files

# create preliminary files for teams
create_other_files.init()
with open(Main.TEAM_DICT_PATH, 'r') as team_dict_file:
    team_dict = load(team_dict_file)


# helper functions
def create_game_logs_file(team_id):
    """
    Creates file for each NBA team containing game info from last season

    :param team_id: ID number of the team
    """
    # team game log
    path = join(Main.TEAM_BASE_PATH, team_dict[team_id] + '.json')
    if not exists(path):
        print("Retrieving team " + team_dict[
            team_id] + " game log data + season stats and creating files ... Please wait.")
        game_logs = team.TeamGameLogs(team_id, '2016-17').json
        with open(path, 'w') as outfile:
            dump(game_logs, outfile)

    # playoff game log
    playoff_path = join(Main.TEAM_PLAYOFF_PATH, team_dict[team_id] + '.json')
    if not exists(playoff_path):
        playoff_games = team.TeamGameLogs(team_id, '2016-17', constants.SeasonType.Playoffs).json
        if len(playoff_games['resultSets'][0]['rowSet']):
            with open(playoff_path, 'w') as playoff_files:
                dump(playoff_games, playoff_files)

    # season stats
    season_path = join(Main.TEAM_SEASON_PATH, team_dict[team_id] + '.json')
    if not exists(season_path):
        season_stats = team.TeamSeasons(team_id).json
        with open(season_path, 'w') as season_files:
            dump(season_stats, season_files)


def init():
    """
    Loop through every single team ID and create a file
    """
    for team_id in team_dict.keys():
        create_game_logs_file(team_id)

    create_other_files.team_name_dict()
