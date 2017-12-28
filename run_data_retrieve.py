"""
The run module that runs all data retrieving
"""

# general imports
from data_retriever import file_check
from data_retriever import team_stat_retriever
from data_retriever import player_stat_retriever
from data_retriever import create_player_rating
from data_retriever import boxscore_retriever


# run
def run():
    file_check.init()
    team_stat_retriever.init()
    player_stat_retriever.init()
    create_player_rating.sort_player_into_team()
    boxscore_retriever.create_boxscore_files()

    return True  # test case use only


if __name__ == "__main__":
    run()  # may take up to 35 minutes to 1 hour depending on internet
