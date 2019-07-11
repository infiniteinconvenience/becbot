import discord
from discord.ext import commands
import pytz
import datetime
import random
import ast

def is_author():
    async def predicate(ctx):
        if not ctx.author.id in [303711794067668994, 108693106194399232]:
            raise commands.CheckFailure(message="bork")
        return True
    return commands.check(predicate)

def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])
    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)
    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)

class BecCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @is_author()
    @commands.command()
    async def exec(self, ctx, *, cmd):
        """Evaluates input.
        Input is interpreted as newline seperated statements.
        If the last statement is an expression, that is the return value.
        Usable globals:
          - `bot`: the bot instance
          - `discord`: the discord module
          - `commands`: the discord.ext.commands module
          - `ctx`: the invokation context
          - `__import__`: the builtin `__import__` function
        Such that `>eval 1 + 1` gives `2` as the result.
        The following invokation will cause the bot to send the text '9'
        to the channel of invokation and return '3' as the result of evaluating
        >eval ```
        a = 1 + 2
        b = a * 2
        await ctx.send(a + b)
        a
        ```
        """
        fn_name = "_eval_expr"

        cmd = cmd.strip("` ")

        # add a layer of indentation
        cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

        # wrap in async def body
        body = f"async def {fn_name}():\n{cmd}"

        parsed = ast.parse(body)
        body = parsed.body[0].body

        insert_returns(body)

        env = {
            'bot': ctx.bot,
            'discord': discord,
            'commands': commands,
            'ctx': ctx,
            '__import__': __import__
        }
        exec(compile(parsed, filename="<ast>", mode="exec"), env)

        result = (await eval(f"{fn_name}()", env))
        await ctx.send(result)    

    @commands.command(aliases = ['infinitime'])
    async def happytime(self, ctx):
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        EST_now = utc_now.astimezone(pytz.timezone('US/Eastern'))
        await ctx.send('It is currently ' + EST_now.strftime("%H:%M:%S") + ' EST')

    @commands.command()
    async def lumitime(self, ctx):
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        cst_now = utc_now.astimezone(pytz.timezone('US/Central'))
        await ctx.send('It is currently ' + cst_now.strftime("%H:%M:%S") + ' CST')

    @commands.command()
    async def ventime(self, ctx):
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        cet_now = utc_now.astimezone(pytz.timezone('Europe/Paris'))
        await ctx.send('It is currently ' + cet_now.strftime("%H:%M:%S") + ' CET')

    #!addcan
    @commands.command(aliases=['addbear','asscan'])
    async def addcan(self, ctx):
        cancount = self.bot.config['cancount']+1
        self.bot.config['cancount'] = cancount
        self.bot.save_config()
        await ctx.send("You place a can on Planet-Lumi. There's now %d cans.  Someone can add another in 35 seconds." % cancount)

    @commands.command()
    async def familyfriendly(self, ctx):
        await ctx.send('https://cozy.galvinism.ink/nff.jpg')

    #hugs
    @commands.command(aliases = ['fight', 'Hug'])
    async def hug(self, ctx, arg):
        await ctx.send('*hugs ' + arg + '*')


    #!hello
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello!")

    #ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
    
    @commands.command()
    async def uranium(self, ctx):
        await ctx.send("Better than !uranus")
    
    @commands.command()
    async def uranus(self, ctx):
        await ctx.send("Better than !uranium")
    
    #funny flipcoin
    @commands.command()
    async def flipcoin(self, ctx):
        responses = [
            'You Lose',
            "it's !coinflip",
            "GAMBLING? In MY good christian server???",
            ]
        await ctx.send(random.choice(responses))
        
     #generates random classpect!
    @commands.command()
    async def classpect(self, ctx):
        classes = [
        'Lord',
        'Muse',
        'Thief',
        'Rogue',
        'Prince',
        'Bard',
        'Witch',
        'Heir',
        'Knight',
        'Page',
        'Maid',
        'Sylph',
        'Mage',
        'Seer',
        ]
        aspects = [
        'Breath',
        'Life',
        'Light',
        'Time',
        'Heart',
        'Rage',
        'Blood',
        'Doom',
        'Void',
        'Space',
        'Mind',
        'Hope',
        ]
        await ctx.send(random.choice(classes) + ' of ' + random.choice(aspects))

    #F
    @commands.command(aliases = ['f'])
    async def F(self, ctx):
        await ctx.send(':regional_indicator_f:')

    #help
    @commands.command()
    async def help(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=yD2FSwTy2lw')

    #!Vengaming
    @commands.command()
    async def vengaming(self, ctx):
        await ctx.send('https://www.youtube.com/Venarion/live')

    #bananapeals!
    @commands.command(aliases = ['bananapeel'])
    async def banappeal(self, ctx):
        await ctx.send('https://docs.google.com/forms/d/e/1FAIpQLScfna7CI_XMEX-szOBC7h_E1XJDSNCjYEYBId69QwuZnITOCw/viewform')
    
    #eat
    @commands.command()
    async def eat(self, ctx):
        await ctx.send('nomf')
    
    #!addjohn
    @commands.command()
    async def addjohn(self, ctx):
        await ctx.send('No')

    #coinflip
    @commands.command()
    async def coinflip(self, ctx):
        await ctx.send("It's !flipcoin")

    #!angery
    @commands.command()
    async def angery(self, ctx):
        await ctx.send('https://pbs.twimg.com/media/CgldEYQU8AA2MPn.jpg')

    #john!
    @commands.command(aliases = ['John'])
    async def john(self, ctx):
        await ctx.send('"Do the Windy Thing!"')

    #Oh No! 
    @commands.command()
    async def ohno(self, ctx):
        await ctx.send('https://media.discordapp.net/attachments/431932541612589077/544587477508161547/Ilikestevenuniversealotbutwhydoi_ad1871fcdc058915b00d12d5968a0d0a.png')

    #orb ORB ORB ORB
    @commands.command()
    async def orb(self, ctx):
        await ctx.send('ORB')

    #Casual sunday
    @commands.command()
    async def ps(self, ctx):
        await ctx.send('P[S] is the unofficial second half of Vol. 10, by the Homestuck Music Team: https://casualsunday.com/album/p-s')

    #Our beloved radio live link nwn
    @commands.command()
    async def radio(self, ctx):
        await ctx.send('https://www.youtube.com/luminantAegis/live')

    #A letter away from RIP in peace
    @commands.command()
    async def rp(self, ctx):
        await ctx.send("We all know role playing isn't allowed here, so you must be looking for this instead! https://mspfa.com/?s=25171&p=1")

    #Sorry Zyr.
    @commands.command()
    async def secretspymachine(self, ctx):
        await ctx.send("We can't do that, but chances are he's offline")

    #Slate my mates and steal my meals!
    @commands.command(aliases = ['Stalemate', 'stealmeal', 'slatemate'])
    async def stalemate(self, ctx):
        await ctx.send('https://mspfa.com/?s=25171&p=1')

    #Tensei senpai~
    @commands.command(aliases = ['tensei=god'])
    async def tensei(self, ctx):
        await ctx.send('https://tenseimusic.bandcamp.com/album/strife-2')

    #Sans
    @commands.command()
    async def undertale(self, ctx):
        await ctx.send(':gift_heart: :heart: :blue_heart: :goat: :yellow_heart: :purple_heart: :sparkling_heart:')

    #Vast Error ! More like... Vast error. (get it? cause happy thinks its bad? ha HA.
    @commands.command(aliases = ['VE', 've', 'readvasterror'])
    async def vasterror(self, ctx):
        await ctx.send('https://mspfa.com/?s=2302&p=1')

    #CANWC
    @commands.command()
    async def canwc(self, ctx):
        await ctx.send('https://mspfa.com/?s=14113&p=1')

    #GH2
    @commands.command()
    async def gh2(self, ctx):
        await ctx.send('https://coolandnewwebcomic.bandcamp.com/album/greatest-hits-2')
    
    @commands.command()
    async def quote(self, ctx, arg):
        num = int(arg)-1
        if num >= len(self.bot.config['quotes']):
            return
        await ctx.send(self.bot.config['quotes'][num])

    #Things that need to @ the author 

    #copper
    @commands.command(aliases=['Copper'], pass_context = True)
    async def copper(self, ctx):
        await ctx.send(ctx.message.author.mention + ': Copper is "Cu" on the periodic table. When read it sounds like "see you", a shortened version of the phrase "See you later", which is commonly used as a sendoff to someone.')
    
    #Honk :o) 
    @commands.command(pass_context = True)
    async def honk(self, ctx):
        await ctx.send(ctx.message.author.mention + ': *honl*')
        
    #Minecraft! Drops a link to the lumicraft discord server 
    @commands.command(aliases=['minecraft', 'lumicraft', 'Lumicraft', 'mc', 'MC'], pass_context = True)
    async def Minecraft(self, ctx):
        await ctx.send(ctx.message.author.mention + " Want to play minecraft with your fellow radio-goers? Join the lumicraft server! https://discord.gg/wWUX8H4")


def setup(bot):
    bot.add_cog(BecCommands(bot))
