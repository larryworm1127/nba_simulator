"""Constant module

This module contains all constants used by this project.

@date: 05/12/2019
@author: Larry Shi
"""
import enum
import json
import os.path
import sys

# ======================================================
# File/Directory Paths Constants
# ======================================================
# Base paths
BASE_PATH = sys.path[0]
ASSET_BASE_PATH = os.path.join(BASE_PATH, 'assets')
TEAM_BASE_PATH = os.path.join(ASSET_BASE_PATH, 'team_stats')
PLAYER_BASE_PATH = os.path.join(ASSET_BASE_PATH, 'player_stats')
GAME_BASE_PATH = os.path.join(ASSET_BASE_PATH, 'game_stats')
PLAYER_RATING_PATH = os.path.join(ASSET_BASE_PATH, 'player_ratings')
SIM_RESULT_PATH = os.path.join(ASSET_BASE_PATH, 'simulated_results')

# Directory paths within base paths
TEAM_PLAYOFF_PATH = os.path.join(TEAM_BASE_PATH, 'playoff_stats')
PLAYER_SEASON_PATH = os.path.join(PLAYER_BASE_PATH, 'season_stats')
TEAM_SEASON_PATH = os.path.join(TEAM_BASE_PATH, 'season_stats')

# File paths
SIM_RANKING_PATH = os.path.join(SIM_RESULT_PATH, 'ranking.json')
SIM_PLAYOFF_PATH = os.path.join(SIM_RESULT_PATH, 'playoff_result.json')

# ======================================================
# Data Constants
# ======================================================
with open(os.path.join(ASSET_BASE_PATH, 'team_dict.json')) as f:
    TEAM_DICT = json.load(f)

with open(os.path.join(ASSET_BASE_PATH, 'conf_list.json')) as f:
    CONF_LIST = json.load(f)

with open(os.path.join(ASSET_BASE_PATH, 'team_name_dict.json')) as f:
    TEAM_NAME_DICT = json.load(f)

with open(os.path.join(ASSET_BASE_PATH, 'player_dict.json')) as f:
    PLAYER_DICT = json.load(f)

with open(os.path.join(ASSET_BASE_PATH, 'game_list.json')) as f:
    GAME_LIST = json.load(f)

with open(os.path.join(ASSET_BASE_PATH, 'division_dict.json')) as f:
    DIVISION_DICT = json.load(f)

# ======================================================
# Boxscore Data Constants
# ======================================================
TEAM_ID_INDEX = 1
PLAYER_STAT_INDEX = 0
TEAM_STAT_INDEX = 1
BOXSCORE_HEADER = ['Player Names', 'P', 'MIN', 'PTS', 'OREB', 'DREB', 'REB',
                   'AST', 'STL', 'BLK', 'FGM', 'FGA', 'FG%', '3PM', '3PA',
                   '3P%', 'FTM', 'FTA', 'FT%', 'TOV', 'PF', '+/-']


class BoxScorePlayerHeaders(enum.IntEnum):
    """Boxscore Player Data Index Enum.
    """
    PLAYER_NAME = 5
    START_POSITION = 6
    MIN = 8
    PTS = 26
    OREB = 18
    DREB = 19
    REB = 20
    AST = 21
    STL = 22
    BLK = 23
    FGM = 9
    FGA = 10
    FG_PCT = 11
    FG3M = 12
    FG3A = 13
    FG3_PCT = 14
    FTM = 15
    FTA = 16
    FT_PCT = 17
    TO = 24
    PF = 25
    PLUS_MINUS = 27


class BoxScoreTeamHeaders(enum.IntEnum):
    """Boxscore Team Data Index Enum.
    """
    MIN = 5
    PTS = 23
    OREB = 15
    DREB = 16
    REB = 17
    AST = 18
    STL = 19
    BLK = 20
    FGM = 6
    FGA = 7
    FG_PCT = 8
    FG3M = 9
    FG3A = 10
    FG3_PCT = 11
    FTM = 12
    FTA = 13
    FT_PCT = 14
    TO = 21
    PF = 22
    PLUS_MINUS = 24


# ======================================================
# Team Season Data Constants
# ======================================================
class TeamSeasonDataIndices(enum.IntEnum):
    """Team Season Data Index Enum.
    """
    TEAM_LOC = 1
    TEAM_NAME = 2
    WINS = 5
    LOSSES = 6
    WLR = 7
    PPG = 32
    FG_PCT = 17
    FG3_PCT = 20
    DREB = 25
    OREB = 24
    REB = 26
    AST = 27
    TOV = 30
    STL = 29
    BLK = 31
    PF = 28


# ======================================================
# Team Game Log Data Constants
# ======================================================
MATCHUP_INDEX = 3
DATE_INDEX = 2


class TeamGameLogDataIndices(enum.IntEnum):
    """Team Game Log Data Index Enum.
    """
    WL = 4
    W = 5
    L = 6
    OREB = 18
    DREB = 19
    REB = 20
    AST = 21
    STL = 22
    BLK = 23
    TOV = 24
    PF = 25
    PTS = 26
