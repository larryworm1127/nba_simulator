# NBA Simulator
[![CircleCI](https://circleci.com/gh/larryworm1127/nba_simulator.svg?style=svg)](https://circleci.com/gh/larryworm1127/nba_simulator)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/37a20c287c1140cdb2b77148447a2cc1)](https://www.codacy.com/app/larryworm1127/nba_simulator?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=larryworm1127/nba_simulator&amp;utm_campaign=Badge_Grade)

## About
The NBA Simulator, is a web based Python program in which it can simulate the 2017-18 season result
and the user can also enjoy viewing the 2016-17 season stats.

## Features
Here is a list of features implemented in the program:
- Local NBA stats downloader
- Dynamic NBA playoff bracket for 2017-18 as well as simulated result for 2018-19 season
- Dynamic stats viewer, which includes the following stats:
    - Wins 
    - Loss
    - Points per Game
    - Rebound per Game
    - Assists per Game
    - Field Goal Percentage
    - 3 Point Percentage
    - Turnover per Game
    - Steals per Game
    - Blocks per Game
    - Fouls per Game
- The above stats are listed for the following categories:
    - Individual team with search bar and stats sorter
    - Box score for individual games played by teams
    - Player performance shown within the box score
- Other features includes:
    - Stats graphs (allow user to see the trend)
    - Team Stats Comparison
    - Team Standings
- Simulation section includes the following features:
    - Simulate entire 2018-19 regular season based on previous years stats
    - Create playoff bracket based on simulated regular season result
    - Simulate 2018-19 playoff
    - Simulated team standing
    
## How to use it
**Python 3.6** is required to run the program.
>To begin using the program, either clone the project or download it as a zip file: \
> ```bash
> git clone https://github.com/larryworm1127/RecipeGenerator.git
> ```
> or use: ```Download Zip``` on GitHub

> Once the project is downloaded, go the the project directory
> ```bash
> ...
> cd nba_simulator   
>```
    
    
> While in the project folder, run:
> ```bash
> $ pipenv sync
> $ pipenv shell
>  ```
> The above creates a virtual environment on the machine and activates the virtual environment 

> After activating the virtual environment, run:
> ```bash
> python manage.py runserver
> ```
> and the following output should appear on console:
> ```
> Performing system checks...
>
> System check identified no issues (0 silenced).
> 
> July 03, 2018 - 01:42:54
> Django version 2.0.6, using settings 'nba_simulator.settings'
> Starting development server at http://127.0.0.1:8000/
> Quit the server with CONTROL-C.
> ```

> The link for the development server shown in the ouput above and clicking it will lead to the website.
> Enjoy!

> **Note: If there are any issues, please report it to the GitHub page, thanks.**
    
## Other Information
**The Project is still under development. Use it at your own risks!**
