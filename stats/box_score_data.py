"""This module creates box score page data"""

# General imports
from os.path import join
from json import load

from constant import GAME_BASE_PATH, TEAM_NAME_DICT, TEAM_DICT
from constant import BoxScorePlayerHeaders, BoxScoreTeamHeaders

# Constants
TEAM_ID_INDEX = 1
PLAYER_STAT_INDEX = 0
TEAM_STAT_INDEX = 1
HEADER = ['Player Names', 'P', 'MIN', 'PTS', 'OREB', 'DREB', 'REB',
          'AST', 'STL', 'BLK', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%',
          'FTM', 'FTA', 'FT%', 'TOV', 'PF', '+/-']

team_headers = ['MIN', 'PTS',
                'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'FGM', 'FGA',
                'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
                'TO', 'PF', 'PLUS_MINUS']

TEAM_HEADERS = ["GAME_ID", "TEAM_ID", "TEAM_NAME", "TEAM_ABBREVIATION",
                "TEAM_CITY", "MIN", "FGM", "FGA", "FG_PCT", "FG3M", "FG3A",
                "FG3_PCT", "FTM", "FTA", "FT_PCT", "OREB", "DREB", "REB", "AST",
                "STL", "BLK", "TO", "PF", "PTS", "PLUS_MINUS"]


# main functions
def create_boxscore_data(game_id):
    path = join(GAME_BASE_PATH, f"{str(game_id)}.json")
    with open(path) as boxscore_file:
        parsed_json = load(boxscore_file)

    result_sets = parsed_json['resultSets']
    player_stats = result_sets[PLAYER_STAT_INDEX]['rowSet']
    team_stats = result_sets[TEAM_STAT_INDEX]['rowSet']

    team1_abb = TEAM_DICT[team_stats[0][TEAM_ID_INDEX]]
    team2_abb = TEAM_DICT[team_stats[1][TEAM_ID_INDEX]]
    team1_name = ' '.join(TEAM_NAME_DICT[team1_abb])
    team2_name = ' '.join(TEAM_NAME_DICT[team2_abb])
    player_boxscore = {team1_abb: [], team2_abb: []}

    # Collect player boxscore data
    for player in player_stats:
        player_data = []
        for category in BoxScorePlayerHeaders:
            data = player[category.value]
            if data is None:
                player_data.append('DNP')
            else:
                player_data.append(data)

        team_abb = TEAM_DICT[player[TEAM_ID_INDEX]]
        player_boxscore[team_abb].append(player_data)

    # Collect team boxscore data
    for team in team_stats:
        team_data = [team[category.value] for category in BoxScoreTeamHeaders]

        # insert placeholders
        team_data.insert(0, 'TOTAL:')
        team_data.insert(1, '')

        team_abb = TEAM_DICT[team[TEAM_ID_INDEX]]
        player_boxscore[team_abb].append(team_data)

    return (
        HEADER,
        player_boxscore[team1_abb],
        player_boxscore[team2_abb],
        team1_name,
        team2_name,
        team1_abb,
        team2_abb
    )
