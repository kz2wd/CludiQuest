
import random


def players_play(player_list, enemy_list):

    dmg_redirection = []

    for i in range(len(player_list)):

        p = player_list[i]
        a = p.turn[0] - 1
        e = p.turn[1] - 1
        t = p.turn[2] - 1

        if a == 0:
            if t < len(enemy_list):
                dmg = round((p.kit.element[e] + p.kit.attack) * enemy_list[t].defense[e] * enemy_list[t].defense[4])
                enemy_list[t].health -= dmg

        elif a == 1:
            if t < len(player_list):
                dmg_redirection.append([i, t])

        elif a == 2:
            if t < len(player_list):
                if player_list[t].kit.health > 0:
                    heal = p.kit.magic
                    if heal + player_list[t].kit.health > player_list[t].kit.hp_max:
                        heal = heal + player_list[t].kit.health - player_list[t].kit.hp_max
                    player_list[t].kit.health += heal

        elif a == 3:
            if t < len(enemy_list):
                dmg = round((p.kit.element[e] + p.kit.magic) * enemy_list[t].defense[e] * enemy_list[t].defense[5])
                enemy_list[t].health -= dmg

    return player_list, enemy_list, dmg_redirection


def enemies_play(player_list, enemy_list, dmg_redirection):

    vulnerable_player = []
    for i in range(len(player_list)):
        if player_list[i].kit.health > 0:
            vulnerable_player.append(i)

    for i in range(len(enemy_list)):
        if enemy_list[i].health > 0:
            not_protected = True
            e = enemy_list[i]
            x = random.randint(0, len(vulnerable_player) - 1)
            for i in range(len(dmg_redirection)):
                if vulnerable_player[x] == dmg_redirection[i][1]:
                    player_list[dmg_redirection[i][0]].kit.health -= e.attack
                    not_protected = False

            if not_protected:
                player_list[vulnerable_player[x]].kit.health -= e.attack

    return player_list


def is_there_a_winner(player_list, enemy_list):
    all_player_are_dead = True
    for i in player_list:
        if i.kit.health > 0:
            all_player_are_dead = False

    all_enemies_are_dead = True
    for i in enemy_list:
        if i.health > 0:
            all_enemies_are_dead = False

    if all_player_are_dead:
        return 813

    elif all_enemies_are_dead:
        return 814
    else:
        return 3
