#import and initialize
from discord.ext.commands import Bot
from discord.ext import commands
import random
import discord
import time
import datetime
from pytz import timezone
import pytz
import asyncio
import os

TOKEN = "NTY1MzAwNDExOTQ3NDE3NjAw.XK0vOw.5pmBVWIbUP7_a098ppfH-DbvO3A"

#commands client creation
BOT_PREFIX = ("!") 

bot = Bot(command_prefix=BOT_PREFIX)
bot.remove_command('help')


#timedate commands

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
hour = utc_now.hour
minute = utc_now.minute
second = utc_now.second

@bot.command(aliases = ['infinitime'])
async def happytime(ctx):
    EST_now = utc_now.astimezone(pytz.timezone('US/Eastern'))
    hour = EST_now.hour
    minute = EST_now.minute
    second = EST_now.second
    await ctx.send('It is currently ' + str(EST_now) + 'EST')

@bot.command()
async def lumitime(ctx):
    cst_now = utc_now.astimezone(pytz.timezone('US/Central'))
    hour = cst_now.hour
    minute = cst_now.minute
    second = cst_now.second
    await ctx.send('It is currently ' + str(cst_now) + 'CST')

@bot.command()
async def ventime(ctx):
    cst_now = utc_now.astimezone(pytz.timezone('Europe/Paris'))
    hour = cst_now.hour
    minute = cst_now.minute
    second = cst_now.second
    await ctx.send('It is currently ' + str(cst_now) + 'CET')

#!addcan
global count
@bot.command(aliases=['addbear','asscan'])
async def addcan(ctx):
    cancount = open("cancount.txt","r")
    count = str(cancount.read())
    acount = int(count)
    newcount = acount + 1
    output = str(newcount)
    await ctx.send(output)
    cancount.close
    cancount = open("cancount.txt", "w")
    cancount.write(output)
    cancount.close
    

#hugs
@bot.command(aliases = ['fight', 'Hug'])
async def hug(ctx, arg):
    await ctx.send('*Hugs ' + arg + '*')


#!hello
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")
    
#ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
    
#funny flipcoin
@bot.command()
async def flipcoin(ctx):
    responses = [
        'You Lose',
        "it's !coinflip",
        "GAMBLING? In MY good christian server???",
        ]
    await ctx.send(random.choice(responses))
    
#F
@bot.command(aliases = ['f'])
async def F(ctx):
    await ctx.send(':regional_indicator_f:')

#help
@bot.command()
async def help(ctx):
    await ctx.send('https://www.youtube.com/watch?v=yD2FSwTy2lw')
    
#!Vengaming
@bot.command()
async def vengaming(ctx):
    await ctx.send('https://www.youtube.com/Venarion/live')
    
#bananapeals!
@bot.command(aliases = ['bananapeel'])
async def banappeal(ctx):
    await ctx.send('https://docs.google.com/forms/d/e/1FAIpQLScfna7CI_XMEX-szOBC7h_E1XJDSNCjYEYBId69QwuZnITOCw/viewform')
#eat
@bot.command()
async def eat(ctx):
    await ctx.send('nomf')
#!addjohn
@bot.command()
async def addjohn(ctx):
    await ctx.send('No')

#coinflip
@bot.command()
async def coinflip(ctx):
    await ctx.send("It's !flipcoin")

#!angery
@bot.command()
async def angery(ctx):
    await ctx.send('https://pbs.twimg.com/media/CgldEYQU8AA2MPn.jpg')

#john!
@bot.command(aliases = ['John'])
async def john(ctx):
    await ctx.send('"Do the Windy Thing!"')

#Oh No! 
@bot.command()
async def ohno(ctx):
    await ctx.send('https://media.discordapp.net/attachments/431932541612589077/544587477508161547/Ilikestevenuniversealotbutwhydoi_ad1871fcdc058915b00d12d5968a0d0a.png')

#orb ORB ORB ORB
@bot.command()
async def orb(ctx):
    await ctx.send('ORB')

#Casual sunday
@bot.command()
async def ps(ctx):
    await ctx.send('P[S] is the unofficial second half of Vol. 10, by the Homestuck Music Team: https://casualsunday.com/album/p-s')

#Our beloved radio live link nwn
@bot.command()
async def radio(ctx):
    await ctx.send('https://www.youtube.com/luminantAegis/live')

#A letter away from RIP in peace
@bot.command()
async def rp(ctx):
    await ctx.send("We all know role playing isn't allowed here, so you must be looking for this instead! https://mspfa.com/?s=25171&p=1")

#Sorry Zyr.
@bot.command()
async def secretspymachine(ctx):
    await ctx.send("We can't do that, but chances are he's offline")

#Slate my mates and steal my meals!
@bot.command(aliases = ['Stalemate', 'stealmeal', 'slatemate'])
async def stalemate(ctx):
    await ctx.send('https://mspfa.com/?s=25171&p=1')

#Tensei senpai~
@bot.command(aliases = ['tensei=god'])
async def tensei(ctx):
    await ctx.send('https://tenseimusic.bandcamp.com/album/strife-2')

#Sans
@bot.command()
async def undertale(ctx):
    await ctx.send(':gift_heart: :heart: :blue_heart: :goat: :yellow_heart: :purple_heart: :sparkling_heart:')

#Vast Error ! More like... Vast error. (get it? cause happy thinks its bad? ha HA.
@bot.command(aliases = ['VE', 've', 'readvasterror'])
async def vasterror(ctx):
    await ctx.send('https://mspfa.com/?s=2302&p=1')
    
#CANWC
@bot.command()
async def canwc(ctx):
    await ctx.send('https://mspfa.com/?s=14113&p=1')

#GH2
@bot.command()
async def gh2(ctx):
    await ctx.send('https://coolandnewwebcomic.bandcamp.com/album/greatest-hits-2')


#Things that need to @ the author 
    
    #copper
@bot.command(aliases=['Copper'],
                 pass_context = True)
async def copper(ctx):
    await ctx.send(ctx.message.author.mention + ': Copper is "Cu" on the periodic table. When read it sounds like "see you", a shortened version of the phrase "See you later", which is commonly used as a sendoff to someone.')
    #Honk :o) 
@bot.command(pass_context = True)
async def honk(ctx):
    await ctx.send(ctx.message.author.mention + ': *honl*')

 
#moderator commands if we ever need any
#@bot.command()
#@commands.has_role('moderator')
#async def ccommand(ctx):
#    await ctx.send('response'

 
#run call
bot.run(TOKEN)
