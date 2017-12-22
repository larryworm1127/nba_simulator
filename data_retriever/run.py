"""
The run module that runs all data retrieving
"""

# general imports
import data_retriever.file_check
import data_retriever.team_stat_retriever
import data_retriever.player_stat_retriever
import data_retriever.create_player_rating
import data_retriever.boxscore_retriever


# run
def run():
    data_retriever.file_check.init()
    data_retriever.team_stat_retriever.init()
    data_retriever.player_stat_retriever.init()
    data_retriever.create_player_rating.sort_player_into_team()
    data_retriever.boxscore_retriever.create_boxscore_files()

    return True  # test case use only

# run()  uncomment to run the data retrieval
#        may take up to 35 minutes to 1 hour depending on internet
