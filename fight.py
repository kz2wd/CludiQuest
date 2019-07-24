
import random


def players_play(player_list, enemy_list):

    dmg_redirection = []

    for i in range(len(player_list)):

        p = player_list[i]
        a = p.turn[0] - 1
        e = p.turn[1] - 1
        t = p.turn[2] - 1

        if a == 0:
            if t <= len(enemy_list):
                dmg = round((p.kit.element[e] + p.kit.attack) * enemy_list[t].defense[e] * enemy_list[t].defense[4])
                enemy_list[t].health -= dmg

        if a == 1:
            if t <= len(player_list):
                dmg_redirection.append([i, t])

        if a == 2:
            if t <= len(player_list):
                heal = p.kit.magic
                if heal + player_list[t].health > player_list[t].max_hp:
                    heal = heal + player_list[t].health - player_list[t].max_hp
                player_list[t].health += heal

        else:
            if t <= len(enemy_list):
                dmg = round((p.kit.element[e] + p.kit.magic) * enemy_list[t].defense[e] * enemy_list[t].defense[5])
                enemy_list[t].health -= dmg

    return player_list, enemy_list, dmg_redirection


def enemies_play(player_list, enemy_list, dmg_redirection):

    for i in range(len(enemy_list)):
        not_protected = True
        e = enemy_list[i]
        x = random.randint(0, len(player_list))
        for i in range(len(dmg_redirection)):
            if x == dmg_redirection[i][1]:
                player_list[dmg_redirection[i][0]].health -= e.attack
                not_protected = False

        if not_protected:
            player_list[x].health -= e.attack

    return player_list


def check_death(player_list, enemy_list):  # ?

    for i in range(4):
        if player_list[i].kit.health < 1:
            player_list[i] = 0

    for i in range(len(enemy_list)):
        if enemy_list[i].health < 1:
            enemy_list[i] = 0

    return player_list, enemy_list