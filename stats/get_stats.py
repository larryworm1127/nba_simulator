"""Get Stats Module

=== Module Description ===
This module contains all functions that supplies corresponding data to front-end
of the website.

@date: 05/27/2019
@author: Larry Shi
"""

from json import load
from os import listdir
from os.path import join
from re import search
from typing import Dict, List, Tuple, Any

from constant import MATCHUP_INDEX, DATE_INDEX, TEAM_ID_INDEX, PLAYER_STAT_INDEX
from constant import TEAM_STAT_INDEX, TEAM_NAME_DICT, TEAM_DICT, DIVISION_DICT
from constant import TEAM_SEASON_PATH, TEAM_BASE_PATH, SIM_RESULT_PATH
from constant import GAME_BASE_PATH
from constant import TeamGameLogDataIndices as TGLIndices
from constant import TeamSeasonDataIndices as TSIndices
from constant import BoxScorePlayerHeaders as BSPHeaders
from constant import BoxScoreTeamHeaders as BSTHeaders
from stats_files import get_id_from_abb


# ==================================================
# All Team Data Functions
# ==================================================
def get_all_team_data(sort: str) -> Dict[str, List]:
    """Creates and sorts data from files so that the web page can read them

    :param sort: the type of sorting the web page requested
    :return: the data to be displayed on the web page
    """
    all_team_data = load_team_season_data()
    data_headers = [
        'TEAM_LOC', 'TEAM_NAME', 'WINS', 'LOSSES', 'PPG', 'FG_PCT', 'FG3_PCT',
        'DREB', 'OREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'PF'
    ]
    result_headers = [
        'Team City', 'Team Name', 'W', 'L', 'PPG', 'FG%', '3P%',
        'DREB', 'OREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'PF'
    ]

    reduced_data = [[row[TSIndices.__members__[header].value]
                     for header in data_headers] for row in all_team_data]

    # sort the data by the requested stats category
    if sort is not None and sort in result_headers:
        index = result_headers.index(sort)
        reverse = False if sort in ['Team City', 'Team Name'] else True
        reduced_data.sort(key=lambda data: data[index], reverse=reverse)

    display_data = {'headers': result_headers, 'rows': reduced_data}

    return display_data


# ==================================================
# Boxscore Data Functions
# ==================================================
def get_boxscore_data(game_id: str) -> Tuple[List, List, str, str, str, str]:
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
        for category in BSPHeaders:
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
        team_data = [team[category.value] for category in BSTHeaders]

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


# ==================================================
# Comparison Data Functions
# ==================================================
def get_comparison_data(teams: str
                        ) -> Tuple[Dict, Dict, List, Dict, Dict, str, str]:
    """Format comparison data to be used in front-end HTML from JSON data files.

    :param teams: the teams string requested from front-end
    :return: a tuple containing all information needed in front-end
    """
    # initialize west conference logo path dictionary and division list
    team_img_path = {"west": {}, "east": {}}
    all_teams = []
    for conf in ["west", "east"]:

        for div in DIVISION_DICT[conf].keys():
            team_img_path[conf][div] = []
            all_teams.append(f"{div} -")

            for team in DIVISION_DICT[conf][div]:
                team_img_path[conf][div].append({team: f"images/{team}.png"})
                all_teams.append(team)

    # the stats comparing dictionaries
    result = {
        "team1": {"W-L R": '', "PPG": '', "FG%": '', "3P%": '', "REB": '',
                  "AST": ''},
        "team2": {"W-L R": '', "PPG": '', "FG%": '', "3P%": '', "REB": '',
                  "AST": ''}
    }
    team1, team2 = '', ''

    # enum does not allow storing special characters so this dict maps enum
    # variables to result display variables
    cat_ref = {"WLR": "W-L R", "PPG": "PPG", "FG_PCT": "FG%",
               "FG3_PCT": "3P%", "REB": "REB", "AST": "AST"}

    # only gather data if request inputs team names
    if teams:
        team1, team2 = teams[:3], teams[3:]
        team_stats = load_team_season_data()
        team1_idx = [str(item[0]) for item in team_stats].index(
            get_id_from_abb(team1))
        team2_idx = [str(item[0]) for item in team_stats].index(
            get_id_from_abb(team2))

        # populate result dict from file data
        for cat, display_cat in cat_ref.items():
            team1_data = team_stats[team1_idx][TSIndices.__members__[cat].value]
            result["team1"][display_cat] = team1_data

            team2_data = team_stats[team2_idx][TSIndices.__members__[cat].value]
            result["team2"][display_cat] = team2_data

    return (
        team_img_path["west"],
        team_img_path["east"],
        all_teams,
        result["team1"],
        result["team2"],
        team1,
        team2
    )


# ==================================================
# Graph Data Functions
# ==================================================
def get_graph_data() -> Tuple[List, List, List, List]:
    """Extract the specific data from files and put them in lists.

    :return: four lists containing stats for different category
    """
    wlr_data = []
    points_data = []
    rebounds_data = []
    assists_data = []

    for team in TEAM_DICT.values():
        with open(join(TEAM_SEASON_PATH, f"{team}.json")) as team_season_file:
            data = load(team_season_file)['resultSets'][0]['rowSet'][-2]

        wlr_data.append((team, data[TSIndices.WLR.value]))
        points_data.append((team, data[TSIndices.PPG.value]))
        rebounds_data.append((team, data[TSIndices.REB.value]))
        assists_data.append((team, data[TSIndices.AST.value]))

    for data in (wlr_data, points_data, rebounds_data, assists_data):
        data.sort(key=lambda ratio: ratio[1], reverse=True)

    return wlr_data, points_data, rebounds_data, assists_data


# ==================================================
# Team Page Data Functions
# ==================================================
def get_team_page_data(team_abb: str) -> Dict[str, List]:
    """Creates the data set from the team game log stats.

    :param team_abb: the team abbreviation of the team
    :return: the data to be displayed on the web page
    """
    with open(join(TEAM_BASE_PATH, team_abb + '.json')) as data_file:
        game_log_data = load(data_file)

    other_teams = [item for item in TEAM_DICT.values()]
    other_teams.remove(team_abb)
    game_dict = {team: [] for team in other_teams}
    game_list = game_log_data['resultSets'][0]['rowSet']

    # Loop through every game
    for team in other_teams:
        for game in game_list:

            # only populate result dict if the <matchup> contains <team>
            data = {}
            matchup = game[MATCHUP_INDEX]
            if search(team, matchup):
                game_url = "/stats/box_score/?gameID=" + game[1]
                data['url'] = game_url
                data['BOXSCORE_HEADER'] = matchup + ' ---- ' + game[DATE_INDEX]
                data['TAB_HEADERS'] = [cat.name for cat in TGLIndices]
                data['DISPLAY'] = [game[cat.value] for cat in TGLIndices]
                game_dict[team].append(data)

    return game_dict


def get_simulated_games(team_abb: str) -> Dict[str, Any]:
    """Creates the data set for simulated games.

    :param team_abb: the team abbreviation of the team
    :return: the data to be displayed on the web page
    """
    with open(join(SIM_RESULT_PATH, team_abb + '.json')) as data_file:
        team_data = load(data_file)

    other_teams = [item for item in TEAM_DICT.values()]
    other_teams.remove(team_abb)
    game_dict = {}

    for team in other_teams:
        single_team = {}
        tab_headers = [f'Game {str(num + 1)}' for num in
                       range(len(team_data[team]))]
        panel_header = team_abb + ' vs. ' + team
        single_team['TAB_HEADERS'] = tab_headers
        single_team['DISPLAY'] = team_data[team]
        single_team['BOXSCORE_HEADER'] = panel_header
        game_dict[team] = single_team

    return game_dict


# ==================================================
# Helper Functions
# ==================================================
def load_team_season_data() -> List:
    """Create a list containing all the team season stats.

    :return: A list containing the data to be sorted and modified
    """
    all_team_lists = []
    for single_file in listdir(TEAM_SEASON_PATH):
        with open(join(TEAM_SEASON_PATH, single_file)) as data_file:
            parsed_json = load(data_file)

        data = parsed_json['resultSets'][0]['rowSet']
        for row in data:
            if row[3] == "2016-17":
                all_team_lists.append(row)

    return all_team_lists
