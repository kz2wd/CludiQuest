import discord
import asyncio
import hero
import Variable

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
            await message.channel.send('```Mhhhh.... Okay```')


client = MyClient()
client.run(Variable.x)