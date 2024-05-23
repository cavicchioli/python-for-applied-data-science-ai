import pandas as pd
import matplotlib.pyplot as plt
import requests

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict


from nba_api.stats.static import teams

nba_teams = teams.get_teams()

dict_nba_team=one_dict(nba_teams)

df_teams=pd.DataFrame(dict_nba_team)

df_warriors=df_teams[df_teams['nickname']=='Warriors']

id_warriors=df_warriors[['id']].values[0][0]


from nba_api.stats.endpoints import leaguegamefinder

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
games = gamefinder.get_data_frames()[0]

games_home=games[games['MATCHUP']=='GSW vs. TOR']
games_away=games[games['MATCHUP']=='GSW @ TOR']

fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()

games_away.plot(x='GAME_DATE',y='PTS', ax=ax)
games_home.plot(x='GAME_DATE',y='PTS', ax=ax)
ax.legend(["away", "home"])
plt.show()