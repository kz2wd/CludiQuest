
import random


def players_play(player_list, enemy_list):

    list_ate = []  # get a list of all actions with target and elements
    for i in range(4):  # number of actions
        list_ate.append([])
        for j in range(4):  # number max of enemies / players
            list_ate[i].append([])
            for k in range(4):  # number of elements
                list_ate[i][j].append(0)

    for i in range(len(player_list)):  # calculation of damage due to elements
        p = player_list[i]
        a = p.turn[0] - 1
        e = p.turn[1] - 1
        t = p.turn[2] - 1

        list_ate[a][t][e] += 1

    print(list_ate)

    bonus_element = []  # action, target, modifier

    for i in range(4):
        for j in range(4):
            x = 0
            for k in range(4):
                x += list_ate[i][j][k]

            if x > 1:  # check the number of action

                nbr_of_0 = 0
                for k in range(4):  # check the number of elements
                    if list_ate[i][j][k] == 0:
                        nbr_of_0 += 1
                if nbr_of_0 == 2:

                    if list_ate[i][j][0] > 0:  # 1 X X X
                        if list_ate[i][j][1] > 0: # 1 1 0 0
                            bonus_element.append([i, j, 0.8])
                        else:  # 1 0 X X
                            if list_ate[i][j][2] > 0:  # 1 0 1 0
                                bonus_element.append([i, j, 1])
                            else:  # 1 0 0 1
                                bonus_element.append([i, j, 1.2])

                    else:  # 0 X X X
                        if list_ate[i][j][1] > 0:  # 0 1 X X
                            if list_ate[i][j][2] > 0:  # 0 1 1 0
                                bonus_element.append([i, j, 1.2])
                            else:  # 0 1 0 1
                                bonus_element.append([i, j, 1])
                        else:  # 0 0 1 1
                            bonus_element.append([i, j, 0.8])

    print("bonus element :")
    print(bonus_element)
    dmg_redirection = []

    for i in range(len(player_list)):  # apply change due to player turn

        p = player_list[i]
        a = p.turn[0] - 1
        e = p.turn[1] - 1
        t = p.turn[2] - 1

        if a == 0:  # physical attack => decrease enemy hp
            if t < len(enemy_list):
                if len(bonus_element) > 0:
                    for j in range(len(bonus_element)):
                        if bonus_element[j][0] == a and bonus_element[j][1] == t:
                            print("attack modified")
                            if p.kit.name == "Archer":
                                if enemy_list[t].defense[4] < 1:
                                    dmg = round((p.kit.element[e] + p.kit.attack) * enemy_list[t].defense[e] *
                                                bonus_element[j][2])
                                else:
                                    dmg = round((p.kit.element[e] + p.kit.attack) * enemy_list[t].defense[e] *
                                                enemy_list[t].defense[4] * bonus_element[j][2])
                            else:
                                dmg = round((p.kit.element[e] + p.kit.attack) * enemy_list[t].defense[e] *
                                            enemy_list[t].defense[4] * bonus_element[j][2])
                            enemy_list[t].health -= dmg
                else:
                    print("same attack")
                    if p.kit.name == "Archer":
                        if enemy_list[t].defense[4] < 1:
                            dmg = round((p.kit.element[e] + p.kit.attack) * enemy_list[t].defense[e])
                        else:
                            dmg = round(
                                (p.kit.element[e] + p.kit.attack) * enemy_list[t].defense[e] *
                                enemy_list[t].defense[4])
                    else:
                        dmg = round((p.kit.element[e] + p.kit.attack) * enemy_list[t].defense[e] *
                                    enemy_list[t].defense[4])
                    enemy_list[t].health -= dmg

        elif a == 1:  # protection => protect an ally
            if t < len(player_list):
                dmg_redirection.append([i, t])

        elif a == 2:  # heal => increase ally hp
            if t < len(player_list):
                if len(bonus_element) > 0:
                    for j in range(len(bonus_element)):
                        if bonus_element[j][0] == a and bonus_element[j][1] == t:
                            print("heal modified")
                            if player_list[t].kit.health > 0:
                                heal = round((p.kit.magic + p.kit.element[e]) * bonus_element[j][2])
                                if player_list[t].kit.health < player_list[t].kit.hp_max:
                                    if heal + player_list[t].kit.health > player_list[t].kit.hp_max:
                                        heal = heal + player_list[t].kit.health - player_list[t].kit.hp_max
                                    player_list[t].kit.health += heal
                else:
                    print("same heal")
                    if player_list[t].kit.health > 0:
                        heal = p.kit.magic + p.kit.element[e]
                        if player_list[t].kit.health < player_list[t].kit.hp_max:
                            if heal + player_list[t].kit.health > player_list[t].kit.hp_max:
                                heal = heal + player_list[t].kit.health - player_list[t].kit.hp_max
                            player_list[t].kit.health += heal

        elif a == 3:  # magical attack => decrease enemy hp
                    if t < len(enemy_list):
                        if len(bonus_element) > 0:
                            for j in range(len(bonus_element)):
                                if bonus_element[j][0] == a and bonus_element[j][1] == t:
                                    print("attack modified")
                                    dmg = round((p.kit.element[e] + p.kit.magic) * enemy_list[t].defense[e] *
                                                enemy_list[t].defense[5] * bonus_element[j][2])
                                    enemy_list[t].health -= dmg
                        else:
                            print("same attack")
                            dmg = round(
                                (p.kit.element[e] + p.kit.magic) * enemy_list[t].defense[e] * enemy_list[t].defense[5])
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
            for j in range(len(dmg_redirection)):
                if vulnerable_player[x] == dmg_redirection[j][1]:
                    player_list[dmg_redirection[j][0]].kit.health -= e.attack
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
