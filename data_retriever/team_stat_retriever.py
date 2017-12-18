# general imports
import json
from os.path import join, exists
from data_retriever import Main
from nba_py import team, constants
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
    if not exists(path):
        print("Retrieving team " + team_dict[team_id] + " game log data + season stats and creating files ... Please wait.")
        game_logs = team.TeamGameLogs(team_id, '2016-17').json
        with open(path, 'w') as outfile:
            json.dump(game_logs, outfile)

    playoff_path = join(Main.TEAM_PLAYOFF_PATH, team_dict[team_id] + '.json')
    if not exists(playoff_path):
        playoff_games = team.TeamGameLogs(team_id, '2016-17', constants.SeasonType.Playoffs).json
        if len(playoff_games['resultSets'][0]['rowSet']):
            with open(playoff_path, 'w') as playoff_files:
                json.dump(playoff_games, playoff_files)

    season_path = join(Main.TEAM_SEASON_PATH, team_dict[team_id] + '.json')
    if not exists(season_path):
        season_stats = team.TeamSeasons(team_id).json
        with open(season_path, 'w') as season_files:
            json.dump(season_stats, season_files)


def create_season_stats_file(team_id):
    path = join(Main.TEAM_SEASON_PATH, team_dict[team_id] + '.json')

    if not exists(path):
        print("Retrieving team season log data and creating files ... Please wait.")
        season_logs = team.TeamSeasons(team_id).json
        with open(path, 'w') as outfile:
            json.dump(season_logs, outfile)


def init():
    """
    Loop through every single team ID and create a file
    """
    for team_id in team_dict.keys():
        create_game_logs_file(team_id)
        create_season_stats_file(team_id)

    file_check.team_name_dict()

