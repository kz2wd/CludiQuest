
import player
import emote


def kit_select(reaction, user, player_list):

    for i in range(len(player_list)):
        if user.id == player_list[i]:
            for j in range(len(emote.kit_choice)):
                if reaction.emoji == emote.kit_choice[j]:
                    player_list[i] = player.Player(user, j, [0, 0, 0])
    return player_list
