import pandas as pd
import warnings
import boto3
warnings.filterwarnings('ignore')

def clean_players(players):
    players["Player"] = players["Player"].str.replace("*","", regex=False)
    players = players[~players["Age"].str.contains("Age")]
    
    return players.to_csv('cleaned_data/clean_players.csv', index=False)

def clean_nickname(nickname):
    new_row = pd.Series(data={'Abbreviation':'TOT', 'Name':'Multiple Teams Total'}, name='40')

    nickname = nickname.append(new_row, ignore_index=False)
    
    return nickname.to_csv('cleaned_data/clean_nickname.csv', index=False)

def clean_teams(teams, nickname):
    teams = teams[~teams["W"].str.contains("Division")]
    teams["Team"] = teams["Team"].str.replace("*", "", regex=False)
    teams["GB"] = teams["GB"].str.replace("","0").astype(float)
    teams = teams.rename(columns={'Team': 'Name'})
    teams = pd.merge(teams, nickname, on='Name', how='left')
    
    return teams.to_csv('cleaned_data/clean_teams.csv', index=False)

def clean_mvp(mvp):
    mvp = mvp.rename(columns={'Pts Won': 'Pts_Won', 'Pts Max': 'Pts_Max'})
    return mvp.to_csv('cleaned_data/clean_mvp.csv', index=False)

def upload_files(file_name, bucket, object_name=None, args=None):
    """
    file_name: name of file on local
    bucket: bucket name
    object_name: name of file on s3
    args: custom args
    """
    client = boto3.client('s3')
    
    if object_name is None:
        object_name = file_name
        
    response = client.upload_file(file_name,bucket,object_name,ExtraArgs = args)
    
    print(response)
    
