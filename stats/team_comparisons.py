from stats.all_team_data import create_team_data


def create_divisions_data():
    west_divisions = {
        "Northwest Division": [{"DEN": "images/DEN.png"}, {"MIN": "images/MIN.png"}, {"OKC": "images/OKC.png"},
                               {"POR": "images/POR.png"}, {"UTA": "images/UTA.png"}],
        "Pacific Division": [{"GSW": "images/GSW.png"}, {"LAC": "images/LAC.png"}, {"LAL": "images/LAL.png"},
                             {"PHX": "images/PHX.png"}, {"SAC": "images/SAC.png"}],
        "Southwest Division": [{"DAL": "images/DAL.png"}, {"HOU": "images/HOU.png"}, {"MEM": "images/MEM.png"},
                               {"NOP": "images/NOP.png"}, {"SAS": "images/SAS.png"}]}
    east_divisions = {
        "Atlantic Division": [{"BOS": "images/BOS.png"}, {"BKN": "images/BKN.png"}, {"NYK": "images/NYK.png"},
                              {"PHI": "images/PHI.png"}, {"TOR": "images/TOR.png"}],
        "Central Division": [{"CHI": "images/CHI.png"}, {"CLE": "images/CLE.png"}, {"DET": "images/DET.png"},
                             {"IND": "images/IND.png"}, {"MIL": "images/MIL.png"}],
        "Southeast Division": [{"ATL": "images/ATL.png"}, {"CHA": "images/CHA.png"},
                               {"MIA": "images/MIA.png"}, {"ORL": "images/ORL.png"},
                               {"WAS": "images/WAS.png"}]}
    all_teams = ["Northwest -", "DEN", "MIN", "OKC", "POR", "UTA", "Pacific -", "GSW", "LAC", "LAL", "PHX", "SAC",
                 "Southwest -", "DAL", "HOU", "MEM", "NOP",
                 "SAS",
                 "Atlantic -", "BOS", "BKN", "NYK", "PHI", "TOR", "Central -", "CHI", "CLE", "DET", "IND", "MIL",
                 "Southeast -", "ATL", "CHA", "MIA", "ORL",
                 "WAS"]
    abbreviations = ["GSW", "SAS", "HOU", "BOS", "CLE", "LAC", "TOR", "UTA", "WAS", "OKC", "ATL", "MEM", "IND", "MIL",
                     "CHI",
                     "MIA", "POR", "DEN", "DET", "CHA", "NOP", "DAL", "SAC", "MIN", "NYK", "ORL", "PHI", "LAL", "PHX",
                     "BKN"]

    data = create_team_data()
    categories = data[0]
    stats = data[1]

    counter = 0
    while counter < 5:
        categories.remove(categories[0])
        counter += 1

    return west_divisions, east_divisions, all_teams, categories, stats, abbreviations
