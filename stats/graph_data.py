"""This module creates data for the stats graphs"""

from json import load
from os.path import join
from typing import Tuple, List

from constant import TEAM_SEASON_PATH, TEAM_DICT
from constant import TeamSeasonDataIndices


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

        wlr_data.append((team, data[TeamSeasonDataIndices.WLR.value]))
        points_data.append((team, data[TeamSeasonDataIndices.PPG.value]))
        rebounds_data.append((team, data[TeamSeasonDataIndices.REB.value]))
        assists_data.append((team, data[TeamSeasonDataIndices.AST.value]))

    for data in (wlr_data, points_data, rebounds_data, assists_data):
        data.sort(key=lambda ratio: ratio[1], reverse=True)

    return wlr_data, points_data, rebounds_data, assists_data
