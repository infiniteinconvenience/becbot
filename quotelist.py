#Quotes!
#import and initialize
from discord.ext.commands import Bot
import random
import discord
TOKEN = "NTY1MzAwNDExOTQ3NDE3NjAw.XK0vOw.5pmBVWIbUP7_a098ppfH-DbvO3A"

#commands client creation
BOT_PREFIX = ("!") 

bot = Bot(command_prefix=BOT_PREFIX)

bot.remove_command('help')



quotelist = [
    '"LET PIDGEY SAY FUCC" - Happygate 2/8/2019"',
    '"i just *yeet*" -Andre 2/22/2019',
    '"youtube algorithms. I\'d rather trust a loaded dice" -Lore 4/9/2019',
    '"Rememeber to uwu your saucy at 4:13 lumitime" -Draconeiric 2/23/29',
    '"Stay away before I break your spinach" -Andre 4/2/19',
    ]; 


#command itself

@bot.command()
async def quote(ctx,arg):
    num = int(arg) 
    await ctx.send(quotelist[num])

bot.run(TOKEN)
