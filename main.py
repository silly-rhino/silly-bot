import os
import discord
from discord.ext import commands

# Set the token.
DISCORD_TOKEN = os.getenv("BOT_TOKEN")
description = '''A silly bot for testing'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?',
                   description=description,
                   intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def Koji(ctx):
    """Who is Koji."""
    await ctx.send("Koji is an old bucket")


@bot.command()
async def Rhino(ctx):
    """Who is Rhino."""
    await ctx.send("Rhino is a silly bucket")


bot.run(DISCORD_TOKEN)
