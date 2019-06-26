
# imports

# public library
import discord
import asyncio

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
            if message.content == msg.start:
                await message.add_reaction(emote.start)
                global chan
                chan = message.channel
        elif message.content == '!!start':
            await message.channel.send(msg.start)

    async def on_reaction_add(self, reaction, user):
        global x
        global chan
        if chan != 0:
            if x == 0:
                x += 1
            elif 0 < x < 5:
                player_list[x - 1] = user.id
                x += 1
                print(player_list)
                print(x - 1)
                if x == 2:  # put 4 instead of 2, but there is just me and the bot :'(
                    print("game starting")

                    game = party.Party(chan, player_list)
                    await chan.send(msg.kit_choose)


x = 0
chan = 0
player_list = [0, 0, 0, 0]

client = MyClient()


client.run(Variable.x)
