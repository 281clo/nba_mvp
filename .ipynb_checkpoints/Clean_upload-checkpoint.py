import pandas as pd
import sqlalchemy as sql
from sqlalchemy import create_engine
import functions as fc
import glob
import boto3

mvp = pd.read_csv('mvps.csv', encoding = 'latin-1', delimiter= ';')
nickname = pd.read_csv('nicknames.csv', encoding = 'latin-1', delimiter= ';')
players = pd.read_csv('players.csv', encoding = 'latin-1', delimiter= ';')
teams = pd.read_csv('teams.csv', encoding = 'latin-1', delimiter= ';')

fc.clean_players(players)
fc.clean_nickname(nickname)
fc.clean_teams(teams, nickname)
fc.clean_mvp(mvp)

client = boto3.client('s3')

try:
    client.create_bucket(Bucket='mvpdata2022')
except:
    pass

files = glob.glob('cleaned_data/*')
print(files)

args = {'ACL': 'public-read'}
for file in files:
    fc.upload_files(file, 'mvpdata2022', args = args)
    print('uploaded ', file)