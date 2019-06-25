
# imports

# public library
import discord
import asyncio

# personals libraries
import hero
import enemies
import party

# private library (token)
import Variable


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author == self.user:
            return
        elif message.content.startswith('!!start'):
            await message.channel.send('!!start')


client = MyClient()
client.run(Variable.x)
