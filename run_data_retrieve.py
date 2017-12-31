"""
The run module that runs all data retrieving
"""

# general imports
from data_retriever import *


# run
def run():
    create_other_files.init()
    team_stat_retriever.init()
    player_stat_retriever.init()
    create_player_rating.sort_player_into_team()
    box_score_retriever.create_box_score_files()

    return True  # test case use only


if __name__ == "__main__":
    run()  # may take up to 35 minutes to 1 hour depending on internet
