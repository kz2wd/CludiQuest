from typing import Any

import discord

import emote
import msg
import player
import kit_selector
import fight
import enemy
import game

import my_token


class Bot(discord.Client):
    def __init__(self, **options: Any):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.presences = True
        super().__init__(intents=intents, **options)

    async def on_ready(self):
        print("{}, {}, is ready".format(self.user.name, self.user.id))
        await client.change_presence(activity=discord.Game(name='Building Dungeons'))

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

            elif message.content == msg.victory:
                await message.add_reaction(emote.go_forward)

            elif message.content == msg.upgrade:
                for i in emote.upgrade:
                    await message.add_reaction(i)

            elif message.content == msg.next_fight:
                await message.add_reaction(emote.go_forward)

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

                    game_1.enemies = enemy.enemies_generation(game_1.fight_round)

                    for i in game_1.players_id:
                        if i.kit.health > 0:
                            await game_1.channel.send(
                                "```{} : {}/{} HP | pd {} | md {} | elements {}```".format(
                                    i.user, i.kit.health, i.kit.hp_max, i.kit.attack, i.kit.magic, i.kit.element))
                        else:
                            await game_1.channel.send("```{} : On the verge of death```".format(i.user))
                    for i in game_1.enemies:
                        if i.health > 0:
                            await game_1.channel.send(
                                "```{} : {}/{} HP | resistance {} | damage {}```".format(
                                    i.name, i.health, i.hp_max, i.defense, i.attack))
                        else:
                            await game_1.channel.send("```{} : Dead```".format(i.name))

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
                            print("player is dead")

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
                            if i.kit.health > 0:
                                i.turn = [0, 0, 0]
                            else:
                                i.turn = [-1, -1, -1]

                        for i in game_1.players_id:
                            if i.kit.health > 0:
                                await game_1.channel.send(
                                    "```{} : {}/{} HP | pd {} | md {} | elements {}```".format(
                                        i.user, i.kit.health, i.kit.hp_max, i.kit.attack, i.kit.magic, i.kit.element))
                            else:
                                await game_1.channel.send("```{} : On the verge of death```".format(i.user))
                        for i in game_1.enemies:
                            if i.health > 0:
                                await game_1.channel.send(
                                    "```{} : {}/{} HP | resistance {} | damage {}```".format(
                                        i.name, i.health, i.hp_max, i.defense, i.attack))
                            else:
                                await game_1.channel.send("```{} : Dead```".format(i.name))

                        await game_1.channel.send(msg.action)
                        await game_1.channel.send(msg.element)
                        await game_1.channel.send(msg.target)

                    elif game_1.state == 813:
                        await game_1.channel.send(msg.defeat +
                                                  "```You survived for {} fight(s)```".format(game_1.fight_round))
                    elif game_1.state == 814:
                        await game_1.channel.send(msg.victory)
                        for i in range(len(game_1.players_id)):
                            game_1.players_id[i].kit.health = game_1.players_id[i].kit.hp_max

                            game_1.players_id[i].kit.up_point = enemy.reward_points(game_1.fight_round)

                            game_1.players_id[i].turn = [0, 0, 0]

        elif game_1.state == 814:
            if user != self.user:

                for i in range(len(game_1.players_id)):
                    if user.id == game_1.players_id[i].user.id:
                        await game_1.channel.send(msg.upgrade)
                        game_1.state = 5

        elif game_1.state == 5:
            if user != self.user:
                for i in range(len(game_1.players_id)):
                    if user.id == game_1.players_id[i].user.id:
                        if game_1.players_id[i].kit.up_point > 0:

                            for j in range(4):  # choose between all 4 elements
                                if reaction.emoji == emote.element[j]:
                                    game_1.players_id[i].kit.element[j] += 1
                                    game_1.players_id[i].kit.up_point -= 1
                                    if game_1.players_id[i].kit.name == "Wizard":
                                        game_1.players_id[i].kit.element[j] += 1
                                    print("element up")

                            if reaction.emoji == emote.upgrade[4]:  # choose between pd / md / health
                                game_1.players_id[i].kit.attack += 1
                                game_1.players_id[i].kit.up_point -= 1
                                if game_1.players_id[i].kit.name == "Archer":
                                    game_1.players_id[i].kit.attack += 1
                                print("dmg up")
                            elif reaction.emoji == emote.upgrade[6]:
                                game_1.players_id[i].kit.magic += 1
                                game_1.players_id[i].kit.up_point -= 1


                                print("magic up")
                            elif reaction.emoji == emote.upgrade[5]:
                                game_1.players_id[i].kit.hp_max += 3
                                game_1.players_id[i].kit.health += 3
                                game_1.players_id[i].kit.up_point -= 1
                                if game_1.players_id[i].kit.name == "Paladin":
                                    game_1.players_id[i].kit.hp_max += 2
                                    game_1.players_id[i].kit.health += 2
                                print("life up")

                        print("checking")
                        all_players_selected = True
                        for j in range(len(game_1.players_id)):
                            print(game_1.players_id[j].kit.up_point)
                            if game_1.players_id[j].kit.up_point > 0:
                                all_players_selected = False
                                print("all player didn't selected")

                        if all_players_selected:
                            await game_1.channel.send(msg.next_fight)
                            game_1.state = 6
                            print("state = 6")
                            print(game_1.fight_round)
                            game_1.fight_round += 1
                            game_1.enemies = enemy.enemies_generation(game_1.fight_round)

        elif game_1.state == 6:
            if user != self.user:
                for i in range(len(game_1.players_id)):
                    if user.id == game_1.players_id[i].user.id:
                        for j in game_1.players_id:
                            if j.kit.health > 0:
                                await game_1.channel.send(
                                    "```{} : {}/{} HP | pd {} | md {} | elements {}```".format(
                                        j.user, j.kit.health, j.kit.hp_max, j.kit.attack, j.kit.magic, j.kit.element))
                            else:
                                await game_1.channel.send("```{} : On the verge of death```".format(j.user))
                        for j in game_1.enemies:
                            if j.health > 0:
                                await game_1.channel.send(
                                    "```{} : {}/{} HP | resistance {} | damage {}```".format(
                                        j.name, j.health, j.hp_max, j.defense, j.attack))
                            else:
                                await game_1.channel.send("```{} : Dead```".format(j.name))
                        await game_1.channel.send(msg.action)
                        await game_1.channel.send(msg.element)
                        await game_1.channel.send(msg.target)
                        game_1.state = 3
                        print("state = 3")

    async def on_reaction_remove(self, reaction, user):
        if game_1.state == 1:
            if reaction.emoji == emote.start:
                game_1.players_id.remove(user.id)
                print(game_1.players_id)


game_1 = game.Game()

client = Bot()

client.run(my_token.token)
