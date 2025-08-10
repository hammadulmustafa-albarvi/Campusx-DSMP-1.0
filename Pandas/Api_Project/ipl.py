import pandas as pd 
import numpy as np 
import json

ipl = pd.read_csv("D:\Campus X\Pandas\Api_Project\ipl-matches.csv")
print(ipl.head())


def teamApi():
    team =  list(ipl['Team1'].unique())
    team_dict  = {
        'teams': team 
    }
    return team_dict


def teamvsteam(Team1,Team2):
    
    teams = list(ipl['Team1'].unique())
    if Team1 in teams and Team2 in teams:
        data_of_matches = ipl[((ipl['Team1'] == Team1)  & (ipl["Team2"] == Team2	)) | ((ipl["Team2"] == Team1)  & (ipl["Team1"] == Team2))]
        team_1_won = data_of_matches['WinningTeam'].value_counts()[Team1]
        team_2_won = data_of_matches['WinningTeam'].value_counts()[Team2]
        total_matches = data_of_matches.shape[0]
        draws = total_matches - (team_2_won+team_1_won)
        response = {
            'total_matches' : str(total_matches),
                Team1 : str(team_1_won),
                Team2       : str(team_2_won),
                'draws'        : str(draws)
        }
    else:
        response = {"Error" : "Invalid Team name"}
    return response



def team_data(team):
    finalResult = {}    
    total_matches = ipl[(ipl['Team1'] == team) | (ipl['Team2'] == team)].shape[0]
    matches_won = ipl[((ipl['Team1'] == team) | (ipl['Team2'] == team)) & (ipl['WinningTeam'] == team )].shape[0]
    matches_draw = ipl[((ipl['Team1'] == team) | (ipl['Team2'] == team)) & (ipl['WinningTeam'].isnull() )].shape[0]
    matches_lost = total_matches - (matches_won + matches_draw)
    title_won = ipl[(ipl['MatchNumber'] == 'Final') & ((ipl['Team1'] == team) | (ipl['Team2'] == team)) & (ipl['WinningTeam'] == team )].shape[0]
    overall_data = {
    "total matches played" : total_matches,
    "won" : matches_won,
    "loss" : matches_lost,
    "draws" : matches_draw,
    "titles won" : title_won
    }
    def team_vs_team(Team1,Team2):

        teams = list(ipl['Team1'].unique())
        if Team1 in teams and Team2 in teams:
            data_of_matches = ipl[((ipl['Team1'] == Team1)  & (ipl["Team2"] == Team2)) | ((ipl["Team2"] == Team1)  & (ipl["Team1"] == Team2))]
            wins = data_of_matches['WinningTeam'].value_counts()

            team_1_won = wins.get(Team1, 0)
            team_2_won = wins.get(Team2, 0)

            total_matches = data_of_matches.shape[0]
            draws = total_matches - (team_2_won+team_1_won)
            response = {
                'total_matches' : str(total_matches),
                    'won' : str(team_1_won),
                    'loss'       : str(team_2_won),
                    'draws'        : str(draws)
            }
        else:
            response = {"Error" : "Invalid Team name"}
        return response
    all_against_teams = {}
    for i in ipl['Team1'].unique():
        if i != team:
            result = team_vs_team(str(team),str(i))
            all_against_teams[i] = result

    finalResult = {
    team : {    "Overall" : overall_data,
    "Against" : all_against_teams}}
    
    return finalResult
