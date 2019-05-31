import requests
import time

def basketballscores():
    t = time.strftime('%Y%m%d')
    url = "'http://data.nba.net/10s/prod/v1/' + t + '/scoreboard.json'"
    scoreboard = requests.get(url)
    scoreboard = scoreboard.json()
    # Created a scoreboard variable and saved it in JSON format. Created a dynamic Time variable so you could get the game that was on that day.
    x = scoreboard['numGames']
    if x:
        print(f"There are {x} games on today.")
        for i in range(x):
            period = scoreboard['games'][i]['period']["current"]
            clock = scoreboard['games'][i]['clock']
            away_team_score = scoreboard['games'][i]['vTeam']['score']
            home_team_score = scoreboard['games'][i]['hTeam']['score']
            away_team = scoreboard['games'][i]['vTeam']['triCode']
            home_team = scoreboard['games'][i]['hTeam']['triCode']        # for i in range(x):
            current_scores =(home_team + ' ' + home_team_score + ' vs ' + away_team + ' ' + 
            away_team_score + ' ' + clock + 'Current period: ' + str(period))
            final_scores =(home_team + ' ' + home_team_score + ' vs ' + away_team + ' ' + 
            away_team_score + ' ' + '        End Period')
            if clock:
                print(current_scores)
            else:
                print(final_scores)
    else:
        print("There are no games on today.")

