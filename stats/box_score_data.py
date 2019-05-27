"""This module creates box score page data"""

# General imports
from os.path import join
from json import load
from typing import Tuple, List

from constant import GAME_BASE_PATH, TEAM_NAME_DICT, TEAM_DICT
from constant import BoxScorePlayerHeaders, BoxScoreTeamHeaders
from constant import PLAYER_STAT_INDEX, TEAM_STAT_INDEX, TEAM_ID_INDEX


# main functions
def create_boxscore_data(game_id: str) -> Tuple[List, List, str, str, str, str]:
    """Format boxscore data to be used in front-end HTML from JSON data files.

    :param game_id: the ID of the game to be displayed.
    :return: a tuple containing all information needed in front-end
    """
    # Load raw JSON data from file
    path = join(GAME_BASE_PATH, f"{str(game_id)}.json")
    with open(path) as boxscore_file:
        parsed_json = load(boxscore_file)

    # Index out the data to be used
    result_sets = parsed_json['resultSets']
    player_stats = result_sets[PLAYER_STAT_INDEX]['rowSet']
    team_stats = result_sets[TEAM_STAT_INDEX]['rowSet']

    # Collect team infos
    team1_abb = TEAM_DICT[str(team_stats[0][TEAM_ID_INDEX])]
    team2_abb = TEAM_DICT[str(team_stats[1][TEAM_ID_INDEX])]
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

        # add to display data
        team_abb = TEAM_DICT[str(player[TEAM_ID_INDEX])]
        player_boxscore[team_abb].append(player_data)

    # Collect team boxscore data
    for team in team_stats:
        team_data = [team[category.value] for category in BoxScoreTeamHeaders]

        # insert placeholders
        team_data.insert(0, 'TOTAL:')
        team_data.insert(1, '')

        team_abb = TEAM_DICT[str(team[TEAM_ID_INDEX])]
        player_boxscore[team_abb].append(team_data)

    return (
        player_boxscore[team1_abb],
        player_boxscore[team2_abb],
        team1_name,
        team2_name,
        team1_abb,
        team2_abb
    )
