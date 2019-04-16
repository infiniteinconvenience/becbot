import discord
from discord.ext import commands

class BecAR(commands.Cog):
    """
    Who threw Becsprite and Autoresponder into the same kernelsprite?!
    """

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        #test == turing
        if message.content.startswith('test'):
            await message.channel.send('turing')
            
        #F 
        if message.content.lower().startswith('f ') or message.content.lower() == "f":
            await message.channel.send(':regional_indicator_f:')
           
        #^^
        if message.content.startswith('^^ ') or message.content.lower() == "^^":
            await message.channel.send('^u^')
            
        #\o/
        if message.content.startswith("\o/"):
            await message.channel.send('https://imgur.com/qJYq4Xn')
          
        #OBAMA IS GONE
        if message.content.lower().startswith('crab'):
            await message.channel.send('https://tenor.com/view/crab-safe-dance-gif-13211112')
        
        #U already know whats going on
        if message.content.lower().startswith('sock ruse'):
            await message.channel.send('it was a DISTACTION')
        
        #Pizza time
        if message.content.lower().startswith("what time is it?"):
            await message.channel.send('https://tenor.com/view/pizza-time-its-delivery-gif-13167414')


        #mod only responses
        if message.content.startswith('chirp'):
            if 'moderator' in [role.name.lower() for role in message.author.roles]: 
                await message.channel.send('chirp chirp!')

        if message.content.startswith('bark'):
            if 'moderator' in [role.name.lower() for role in message.author.roles]: 
                await message.channel.send('bork')

        if message.content.startswith('bear'):
            if 'moderator' in [role.name.lower() for role in message.author.roles]: 
                await message.channel.send(':bear:')

def setup(bot):
    bot.add_cog(BecAR(bot))