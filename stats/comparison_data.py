"""This module formats data needed for team comparison page"""

# General imports
from typing import Tuple, Dict, List

from constant import DIVISION_DICT
from constant import TeamSeasonDataIndices as Indices
from stats_files import get_id_from_abb
from .all_team_data import load_team_season_data


def create_comparison_data(teams: str
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
        team1_index = [str(item[0]) for item in team_stats
                       ].index(get_id_from_abb(team1))
        team2_index = [str(item[0]) for item in team_stats
                       ].index(get_id_from_abb(team2))

        # populate result dict from file data
        for cat, display_cat in cat_ref.items():
            team1_data = team_stats[team1_index][Indices.__members__[cat].value]
            result["team1"][display_cat] = team1_data

            team2_data = team_stats[team2_index][Indices.__members__[cat].value]
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
