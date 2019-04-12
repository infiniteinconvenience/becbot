import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

TOKEN = "NTY1MzAwNDExOTQ3NDE3NjAw.XK0vOw.5pmBVWIbUP7_a098ppfH-DbvO3A"

Client = discord.Client()
client = commands.Bot(command_prefix = '!')


#No-no words list!
Client = discord.Client()
chat_filter=['swear', 'cunt','twat','slut', 'porn','pornography','nigger','nigga', 'fag', 'faggot', 'whore']

@client.event
async def on_message(message):
    if message.content.lower() in chat_filter:
            await message.delete()
            await message.channel.send("{}, https://www.youtube.com/watch?v=hpigjnKl7nI".format(message.author.mention))


client.run(TOKEN)
