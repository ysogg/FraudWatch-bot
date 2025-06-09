
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands
from discord import Guild

load_dotenv()

TOKEN = os.getenv("TOK")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def fraud(ctx, name: discord.User):
    role = ctx.guild.get_role(1381733158286004396) #Role ID
    await name.add_roles(role)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


bot.run(TOKEN)


