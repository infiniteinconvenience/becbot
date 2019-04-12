#Bot's autoresponding capabilities are run through here
import discord
from discord.ext import commands

TOKEN = "NTY1MzAwNDExOTQ3NDE3NjAw.XK0vOw.5pmBVWIbUP7_a098ppfH-DbvO3A"

class MyClient(discord.Client):

#autoresponses used by anybody. Mod only added later and will be tricky
    
    async def on_message(self, message):
        #stops bot from getting stuck talking to itself
        if message.author.id == self.user.id:
            return
        
        #test == turing
        if message.content.startswith('test'):
            await message.channel.send('turing'.format(message))
            
        #F
        if message.content.startswith('F '):
            await message.channel.send(':regional_indicator_f:'.format(message))
           
        if message.content.startswith('f '):
            await message.channel.send(':regional_indicator_f:'.format(message))
           
        #^^
        if message.content.startswith('^^'):
            await message.channel.send('^u^'.format(message))
            
        #\o/
        if message.content.startswith("\o/"):
            await message.channel.send('https://imgur.com/qJYq4Xn'.format(message))
          
        #OBAMA IS GONE
        if message.content.startswith('crab'):
            await message.channel.send('https://tenor.com/view/crab-safe-dance-gif-13211112'.format(message))
        #U already know whats going on
        if message.content.startswith('sock ruse'):
            await message.channel.send('it was a DISTACTION'.format(message))
        #Pizza time
        if message.content.startswith("What time is it?"):
            await message.channel.send('https://tenor.com/view/pizza-time-its-delivery-gif-13167414')


#mod only responses
        if message.content.startswith('chirp'):
            if 'moderator' in [role.name.lower() for role in message.author.roles]: 
                await message.channel.send('chirp chirp!'.format(message))
        if message.content.startswith('bark'):
            if 'moderator' in [role.name.lower() for role in message.author.roles]: 
                await message.channel.send('bork'.format(message))
        if message.content.startswith('bear'):
            if 'moderator' in [role.name.lower() for role in message.author.roles]: 
                await message.channel.send(':bear:'.format(message))




client = MyClient()
client.run(TOKEN)
