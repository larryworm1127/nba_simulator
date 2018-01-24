"""
The run module that runs all data retrieving
"""

# general imports
from stats_files import *


# run
def run():
    create_other_files.init()
    team_stats.init()
    player_stats.init()
    create_player_rating.sort_player_into_team()
    box_score.create_box_score_files()

    return True  # test case use only


if __name__ == "__main__":
    run()  # may take up to 35 minutes to 1 hour depending on internet
