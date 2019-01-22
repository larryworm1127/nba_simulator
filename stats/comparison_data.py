"""This module formats data needed for team comparison page"""

# general imports
from stats.all_team_data import get_data


def create_divisions_data(compare):
    # initialize west conference logo path dictionary
    west_divisions = {
        "Northwest Division": [{"DEN": "images/DEN.png"},
                               {"MIN": "images/MIN.png"},
                               {"OKC": "images/OKC.png"},
                               {"POR": "images/POR.png"},
                               {"UTA": "images/UTA.png"}],
        "Pacific Division": [{"GSW": "images/GSW.png"},
                             {"LAC": "images/LAC.png"},
                             {"LAL": "images/LAL.png"},
                             {"PHX": "images/PHX.png"},
                             {"SAC": "images/SAC.png"}],
        "Southwest Division": [{"DAL": "images/DAL.png"},
                               {"HOU": "images/HOU.png"},
                               {"MEM": "images/MEM.png"},
                               {"NOP": "images/NOP.png"},
                               {"SAS": "images/SAS.png"}]
    }

    # initialize east conference logo path dictionary
    east_divisions = {
        "Atlantic Division": [{"BOS": "images/BOS.png"},
                              {"BKN": "images/BKN.png"},
                              {"NYK": "images/NYK.png"},
                              {"PHI": "images/PHI.png"},
                              {"TOR": "images/TOR.png"}],
        "Central Division": [{"CHI": "images/CHI.png"},
                             {"CLE": "images/CLE.png"},
                             {"DET": "images/DET.png"},
                             {"IND": "images/IND.png"},
                             {"MIL": "images/MIL.png"}],
        "Southeast Division": [{"ATL": "images/ATL.png"},
                               {"CHA": "images/CHA.png"},
                               {"MIA": "images/MIA.png"},
                               {"ORL": "images/ORL.png"},
                               {"WAS": "images/WAS.png"}]
    }

    # initialize division list
    all_teams = ["Northwest -", "DEN", "MIN", "OKC", "POR", "UTA",
                 "Pacific -", "GSW", "LAC", "LAL", "PHX", "SAC",
                 "Southwest -", "DAL", "HOU", "MEM", "NOP", "SAS",
                 "Atlantic -", "BOS", "BKN", "NYK", "PHI", "TOR",
                 "Central -", "CHI", "CLE", "DET", "IND", "MIL",
                 "Southeast -", "ATL", "CHA", "MIA", "ORL", "WAS"]
    abbreviations = ["ATL", "BKN", "BOS", "CHA", "CHI", "CLE", "DAL", "DEN",
                     "DET", "GSW", "HOU", "IND", "LAC", "LAL",
                     "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", "OKC", "ORL",
                     "PHI", "PHX", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]

    # the stats comparing dictionaries
    categories1 = {"W-L R": '', "PPG": '', "FG%": '', "3P%": '', "REB": '',
                   "AST": ''}
    categories2 = {"W-L R": '', "PPG": '', "FG%": '', "3P%": '', "REB": '',
                   "AST": ''}
    categories_index = [7, 32, 17, 20, 26, 27]

    stats = get_data()
    stats1 = []
    stats2 = []
    team1 = ''
    team2 = ''
    counter = 0

    # if user selected the two teams and pressed the compare button
    if compare is not None:
        team1 = compare[0:3]
        team2 = compare[3:6]
        temp1 = stats[abbreviations.index(team1)]
        temp2 = stats[abbreviations.index(team2)]
        for each in categories_index:
            stats1.append(temp1[each])
            stats2.append(temp2[each])
        for key in categories1.keys():
            categories1[key] = stats1[counter]
            categories2[key] = stats2[counter]
            counter += 1

    return west_divisions, east_divisions, all_teams, categories1, categories2, abbreviations, team1, team2
