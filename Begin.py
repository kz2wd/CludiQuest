# imports

# public library
import discord
import asyncio

# personals libraries
import enemy
import party
import msg
import emote
import kit_selector
import player
import fight

# private library (token)
import my_token


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
                global x
                chan = message.channel
                x = 0

            elif message.content == msg.kit_choose:
                for i in emote.kit_choice:
                    await message.add_reaction(i)
                await message.add_reaction(emote.go_forward)

            elif message.content == msg.action:
                for i in emote.action:
                    await message.add_reaction(i)

            elif message.content == msg.element:
                for i in emote.element:
                    await message.add_reaction(i)

            elif message.content == msg.target:
                for i in emote.target:
                    await message.add_reaction(i)

        elif message.content == '!!start':
            await message.channel.send(msg.start)

    async def on_reaction_add(self, reaction, user):

        global x
        global chan
        global player_list

        if chan != 0:

            if reaction.emoji == emote.start:

                if x == 0:

                    player_list = [0, 0, 0, 0]
                    x += 1

                elif 0 < x < 5:

                    for i in player_list:  # check if the player is already in
                        if user.id == i:
                            print("redundant id")
                            return

                    player_list[x - 1] = user.id
                    print(player_list)
                    print(x - 1)
                    x += 1
                    if x == 5:  # put 5 instead of 2, but there is just me and the bot :'(

                        if user != self.user:
                            print("game starting")

                            game = party.Party(chan, player_list)
                            await chan.send(msg.kit_choose)
                            x += 1
            else:

                if user != self.user:

                    for i in range(4):  # just for the tests
                        if type(player_list[i]) != player.Player:

                            print(type(player_list[0]))

                            player_list = kit_selector.kit_select(reaction, user, player_list)

                        else:

                            print("fight")
                            global enemy_list
                            print(enemy_list)
                            if enemy_list == [0]:
                                enemy_list = enemy.enemies_generation()

                            global turn_counter
                            global next_turn

                            if turn_counter < next_turn:

                                await chan.send("```" \
                                                + str(player_list[0].user) + " : "+str(player_list[0].kit.health)+" ❤\n" \
                                                + str(player_list[1].user) + " : "+str(player_list[1].kit.health)+" ❤\n" \
                                                + str(player_list[2].user) + " : "+str(player_list[2].kit.health)+" ❤\n" \
                                                + str(player_list[3].user) + " : "+str(player_list[3].kit.health)+" ❤\n" \
                                                + "```")  # can't put it in msg.py => player_list = undefined

                                for j in enemy_list:
                                    await chan.send("```" + str(j.name) + " : " + str(j.health) + " ❤```")

                                await chan.send(msg.action)
                                await chan.send(msg.element)
                                await chan.send(msg.target)

                                turn_counter += 1
                                print("turn counter")
                                print(turn_counter)

                            check = 0
                            for i in range(len(player_list)):  # len(player_list), not 1
                                if user == player_list[i].user:

                                    for o in range(len(player_list[i].turn)):
                                        if player_list[i].turn[o] == 0:

                                            for k in range(len(emote.action)):
                                                if reaction.emoji == emote.action[k]:
                                                    player_list[i].turn[0] = k + 1  # between 1 and 4

                                            for l in range(len(emote.element)):
                                                if reaction.emoji == emote.element[l]:
                                                    player_list[i].turn[1] = l + 1

                                            for m in range(len(emote.target)):
                                                if reaction.emoji == emote.target[m]:
                                                    player_list[i].turn[2] = m + 1

                                            print("player list turn")
                                            print(player_list[0].turn)

                                        else:
                                            check += 1
                                            print("check = {}".format(check))

                            if check == 12:
                                global player_turn
                                if player_turn < next_turn:
                                    player_turn += 1

                                    player_list, enemy_list = fight.players_play(player_list, enemy_list)
                                    player_list = fight.enemies_play(player_list, enemy_list)
                                    next_turn += 1


x = 0
chan = 0
player_list = [0, 0, 0, 0]
enemy_list = [0]

turn_counter = 0
next_turn = 1
player_turn = 0

client = MyClient()

client.run(my_token.token)

