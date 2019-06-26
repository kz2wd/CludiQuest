
# imports

# public library
import discord
import asyncio
import time

# personals libraries
import hero
import enemies
import party
import msg
import emote

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
        elif message.content == '!!start':
            await message.channel.send(msg.start)
            await message.add_reaction(emote.start)


client = MyClient()
client.run(Variable.x)
