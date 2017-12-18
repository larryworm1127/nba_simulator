from data_retriever import file_check, team_stat_retriever, player_stat_retriever, game_list_retriever, \
    create_player_rating, boxscore_retriever


def run():
    file_check.init()
    team_stat_retriever.init()
    player_stat_retriever.init()
    game_list_retriever.init()
    create_player_rating.sort_player_into_team()
    boxscore_retriever.create_game_log_profile()

    return True  # test case use only
