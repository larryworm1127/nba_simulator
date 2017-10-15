from nba_py import team
from os.path import join
import json

TEAM_BASE_PATH = "C:/nba_simulator/assets/team_stats/"
PLAYER_BASE_PATH = "C:/nba_simulator/assets/player_stats/"

teams = team.TeamList().info()
TEAM_DICT = {teams[num]['TEAM_ID']: teams[num]['ABBREVIATION'] for num in range(30)}

player_file_path = join(PLAYER_BASE_PATH, 'player_list.json')
with open(player_file_path) as player_file:
    player_list = json.load(player_file)
PLAYER_DICT = {player_list['resultSets'][0]['rowSet'][num][0]: player_list['resultSets'][0]['rowSet'][num][6]
               for num in range(len(player_list['resultSets'][0]['rowSet']))}


