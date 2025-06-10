
import os
from dotenv import load_dotenv
import pandas as pd
import csv
from datetime import datetime

import discord
from discord.ext import commands
from discord import Guild

load_dotenv()

TOKEN = os.getenv("TOK")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


def logUserEpoch(user):
    with open('epochs.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([str(user), datetime.today().strftime('%Y-%m-%d %H:%M:%S')])

@bot.command()
async def fraud(ctx, user: discord.User):
    role = ctx.guild.get_role(1381733158286004396) #Role ID
    await user.add_roles(role)
    logUserEpoch(user)

@bot.command()
async def rmfraud(ctx, user: discord.User):
    role = ctx.guild.get_role(1381733158286004396)
    await user.remove_roles(role)

    df = pd.read_csv('epochs.csv')

    df_s = df

    df_s.set_index('user', inplace=True)
    
    df_s = df_s.drop(str(user))

    df_s.to_csv('epochs.csv')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


bot.run(TOKEN)


