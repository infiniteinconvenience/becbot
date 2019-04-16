import discord
from discord.ext import commands

class BecMod(commands.Cog):
    """
    The best boye
    """

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower() in self.bot.config['filter']:
            await message.delete()
            await message.channel.send("{}, https://www.youtube.com/watch?v=hpigjnKl7nI".format(message.author.mention))

def setup(bot):
    bot.add_cog(BecMod(bot))