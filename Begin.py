import discord
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.content.startswith('$help'):
            await message.channel.send('```Nothing here...```')

    async def on_message(self, message):
        if message.content.startswith('$play'):
            await message.channel.send('```Mhhhh.... Okay thats```')

class discord.Message:


client = MyClient()
client.run('NTkyNzgwOTMyODM5MjQzNzgy.XREUaw.uX3yVNoSNYFmBPsREVqJ1MupWag')