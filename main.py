import discord

import emote
import msg
import player
import kit_selector
import party
import fight
import enemy
import game

import my_token


class Bot(discord.Client):
    async def on_ready(self):
        print("{}, {}, is ready".format(self.user.name, self.user.id))

    async def on_message(self, message):
        if message.author == self.user:
            if message.content == msg.start:
                await message.add_reaction(emote.start)
                await message.add_reaction(emote.go_forward)

            elif message.content == msg.kit_choose:
                for i in emote.kit_choice:
                    await message.add_reaction(i)

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
            if game_1.state == 0:
                await message.channel.send(msg.start)
                game_1.state = 1
                print("state = 1")
                game_1.channel = message.channel
            elif 5 > game_1.state > 2:
                if message.author == game_1.players_id[0].user.id:
                    game_1.__init__()
                    await message.channel.send(msg.start)
                    game_1.state = 1
                    print("state = 1")
                    game_1.channel = message.channel
            elif game_1.state > 5:
                game_1.__init__()
                await message.channel.send(msg.start)
                game_1.state = 1
                print("state = 1")
                game_1.channel = message.channel


    async def on_reaction_add(self, reaction, user):
        if game_1.state == 1:
            if user != self.user:
                if reaction.emoji == emote.start:
                    if len(game_1.players_id) < 5:
                        game_1.players_id.append(user.id)
                        print(game_1.players_id)
                elif reaction.emoji == emote.go_forward:
                    if len(game_1.players_id) > 0:
                        if user.id == game_1.players_id[0]:
                            game_1.state = 2
                            print("state = 2")
                            await game_1.channel.send(msg.kit_choose)

        elif game_1.state == 2:
            if user != self.user:
                for i in game_1.players_id:
                    if type(i) != player.Player:
                        game_1.players_id = kit_selector.kit_select(reaction, user, game_1.players_id)

                all_players_selected = True
                for i in game_1.players_id:
                    if type(i) != player.Player:
                        all_players_selected = False

                if all_players_selected:
                    game_1.state = 3
                    print("state = 3")

                    game_1.enemies = enemy.enemies_generation()

                    for i in game_1.players_id:
                        await game_1.channel.send("```{} : {} HP ```".format(i.user, i.kit.health))
                    for i in game_1.enemies:
                        await game_1.channel.send("```{} : {} HP ```".format(i.name, i.health))
                    await game_1.channel.send(msg.action)
                    await game_1.channel.send(msg.element)
                    await game_1.channel.send(msg.target)

        elif game_1.state == 3:
            if user != self.user:

                for i in range(len(game_1.players_id)):
                    if user.id == game_1.players_id[i].user.id:

                        if game_1.players_id[i].kit.health > 0:

                            for j in range(len(game_1.players_id[i].turn)):
                                if game_1.players_id[i].turn[j] == 0:

                                    for k in range(len(emote.action)):
                                        if reaction.emoji == emote.action[k]:
                                            game_1.players_id[i].turn[0] = k + 1

                                    for l in range(len(emote.element)):
                                        if reaction.emoji == emote.element[l]:
                                            game_1.players_id[i].turn[1] = l + 1

                                    for m in range(len(emote.target)):
                                        if reaction.emoji == emote.target[m]:
                                            game_1.players_id[i].turn[2] = m + 1
                        else:
                            game_1.players_id[i].turn = [-1, -1, -1]

                all_players_played = True
                for i in range(len(game_1.players_id)):
                    for j in range(len(game_1.players_id[i].turn)):
                        if game_1.players_id[i].turn[j] == 0:
                            all_players_played = False

                if all_players_played:
                    game_1.state = 4
                    print("state = 4")
                    game_1.players_id, game_1.enemies, dmg_redirection = fight.players_play(game_1.players_id,
                                                                                            game_1.enemies)
                    game_1.players_id = fight.enemies_play(game_1.players_id, game_1.enemies, dmg_redirection)

                    game_1.state = fight.is_there_a_winner(game_1.players_id, game_1.enemies)

                    if game_1.state == 3:
                        for i in game_1.players_id:
                            i.turn = [0, 0, 0]

                        for i in game_1.players_id:
                            await game_1.channel.send("```{} : {} HP ```".format(i.user, i.kit.health))
                        for i in game_1.enemies:
                            await game_1.channel.send("```{} : {} HP ```".format(i.name, i.health))
                        await game_1.channel.send(msg.action)
                        await game_1.channel.send(msg.element)
                        await game_1.channel.send(msg.target)

                    elif game_1.state == 813:
                        await game_1.channel.send(msg.defeat)
                    elif game_1.state == 814:
                        await game_1.channel.send(msg.victory)

    async def on_reaction_remove(self, reaction, user):
        if game_1.state == 1:
            if reaction.emoji == emote.start:
                game_1.players_id.remove(user.id)
                print(game_1.players_id)


game_1 = game.Game()

client = Bot()

client.run(my_token.token)
