import sys
import math

# Initialisation

fuire = False

action1_a = ""
action1_b = ""
action1_c = ""

action2 = "0"

dic_sites = {}

dic_sites_owner = {}

distance_sites = {}

# Mes batiments
liste_batiment = []

mines = {}
mine_fin = {}

tour = {}
position_tour = {}
distance_tour = {}
distance_tour_chevalier = {}

caserne_chevalier = {}
caserne_archer = {}
caserne_geant = {}

# Batiments adverse
ennemie_batiment = {}

ennemie_mines = {}
ennemie_tour = {}

ennemie_caserne_chevalier = {}
ennemie_caserne_archer = {}
ennemie_caserne_geant = {}

# Mes unités
dic_unit = {}

reine_x = ""
reine_x = ""
reine_pv = ""

chevalier = {}
archer = {}
geant = {}

# Unitées adverse
ennemie_reine_x = ""
ennemie_reine_y = ""
ennemie_reine_pv = ""

ennemie_chevalier = {}
pos_chevalier = {}
distance_chevalier = {}

ennemie_archer = {}
ennemie_geant = {}

s_gold = 0

# debug
turn = 0

num_sites = int(input())
for i in range(num_sites):
    site_id, x, y, radius = [int(j) for j in input().split()]
    dic_sites.update({site_id : [x, y]}) # dictionnaire de tous les sites et leurs positions

while True:

    action1_a = ""
    action1_b = ""
    action1_c = ""

    liste_batiment.clear()

    mines.clear()
    mine_fin.clear()

    tour.clear()
    proche_tour = ""
    position_tour.clear()
    distance_tour.clear()
    distance_tour_chevalier.clear()
    caserne_chevalier.clear()
    caserne_archer.clear()
    caserne_geant.clear()

    chevalier.clear()
    archer.clear()
    geant.clear()

    ennemie_chevalier.clear()
    pos_chevalier.clear()
    distance_chevalier.clear()
    distance_tour_chevalier.clear()

    fuire = False

    turn += 1

    if turn > 1:
        s_gold = gold

    gold, touched_site = [int(i) for i in input().split()]
    for i in range(num_sites):
        site_id, gold_remaining, max_mine_size, structure_type, owner, param_1, param_2 = [int(j) for j in input().split()]
        dic_sites_owner.update({site_id : [structure_type, owner, param_1, param_2, gold_remaining, max_mine_size]}) # dictionnaire des paramètres des sites

    num_units = int(input())
    for i in range(num_units):
        x, y, owner, unit_type, health = [int(j) for j in input().split()]
        dic_unit.update({i : {owner : {unit_type : [x, y, health]}}}) # dictionnaire des paramètres des unitées

    # Récupération des valeurs des unitées
    for i, sub_dic1 in dic_unit.items():
        for owner, sub_dic2 in sub_dic1.items():
            if owner == 0: # Mes unitées
                for unit_type, val in sub_dic2.items():
                    if unit_type == -1: # Reine
                        reine_x = val[0]
                        reine_y = val[1]
                        reine_pv = val[2]
                    if unit_type == 0: # Chevalier
                        chevalier.update({i : [val[0], val[1], val[2]]})
                    if unit_type == 1: # Archer
                        archer.update({i : [val[0], val[1], val[2]]})
                    if unit_type == 2: # Géant
                        geant.update({i : [val[0], val[1], val[2]]})
            elif owner == 1: # Unitées adverse
                for unit_type, val in sub_dic2.items():
                    if unit_type == -1: # Reine
                        ennemie_reine_x = val[0]
                        ennemie_reine_y = val[1]
                        ennemie_reine_pv = val[2]
                    if unit_type == 0: # Chevalier
                        ennemie_chevalier.update({i : [val[0], val[1], val[2]]})
                    if unit_type == 1: # Archer
                        ennemie_archer.update({i : [val[0], val[1], val[2]]})
                    if unit_type == 2: # Géant
                        ennemie_geant.update({i : [val[0], val[1], val[2]]})

    # Récupération des valeurs des sites
    for site_id, val in dic_sites_owner.items():
        mine_fin.update({site_id : val[4]})
        if val[1] == -1: # Pas de batiment
            continue
        if val[1] == 0: # Mes batiment
            liste_batiment.append(site_id)
            if val[0] == 0: # Mines
                mines.update({site_id : [val[2], val[4], val[5]]})
            if val[0] == 1: # Tour
                tour.update({site_id : [val[2], val[3]]})
            if val[0] == 2: # Caserne
                if val[3] == 0: # Caserne chevalier
                    caserne_chevalier.update({site_id : val[2]})
                if val[3] == 1: # Caserne archer
                    caserne_archer.update({site_id : val[2]})
                if val[3] == 2: # Caserne géant
                    caserne_geant.update({site_id : [val[2], val[4], val[5]]})
        if val[1] == 1: # Batiment adverse
            if val[0] == 0: # Mines
                ennemie_mines.update({site_id : val[2]})
            if val[0] == 1: # Tour
                ennemie_tour.update({site_id : [val[2], val[3]]})
            if val[0] == 2: # Caserne
                if val[3] == 0: # Caserne chevalier
                    ennemie_caserne_chevalier.update({site_id : val[2]})
                if val[3] == 1: # Caserne archer
                    ennemie_caserne_archer.update({site_id : val[2]})
                if val[3] == 2: # Caserne géant
                    ennemie_caserne_geant.update({site_id : val[2]})

    # Récupération des positions de mes tour
    for site_id in tour.keys():
        for i, position in dic_sites.items():
            if site_id == i:
                position_tour.update({site_id : [position[0], position[1]]})

# DEPLACEMENT DE LA REINE

    # Calcul de la distance Reine / Site
    for site_id, val in dic_sites.items():
        distance_sites.update({site_id : math.sqrt((reine_x - val[0])**2 + (reine_y - val[1])**2)})

    # Calcule de la distance Reine / Chevalier
    if len(ennemie_chevalier) > 0:
        for i, val in ennemie_chevalier.items():
            distance_chevalier.update({i : math.sqrt((reine_x - val[0])**2 + (reine_y - val[1])**2)})

    # Calcul de la distance Reine / Tour
    if len(tour) > 0:
        for site_id, position in position_tour.items():
            distance_tour.update({site_id : math.sqrt((reine_x - position[0])**2) + (reine_y - position[1])**2})

    # Condition de fuite selon la distance Reine / Chevalier vers la tour la plus proche
    for distance in distance_chevalier.values():
        if min(distance_chevalier.values()) < 400:
            action1_a = "MOVE"
            fuire = True
        else:
            fuire = False
    
    if len(tour) > 0 and fuire == True:
        proche_tour = min(distance_tour, key=distance_tour.get)
        for site_id, position in position_tour.items():
            if proche_tour == site_id:
                action1_b = position[0]
                action1_c = position[1]
            if touched_site == site_id:
                action1_a = "BUILD"
                action1_b = touched_site
                action1_c = "TOWER"
    elif len(tour) == 0 and fuire == True:
        for site_id, distance in distance_sites.items():
            if min(distance_sites.values()) == distance:
                action1_a = "BUILD"
                action1_b = site_id
                action1_c = "TOWER"

    print("toto", file=sys.stderr, flush=True)

    # Suppression du dictionnaire des sites
    for site_id in tour.keys():
        if site_id in distance_sites:
            distance_sites.pop(site_id)
    for site_id in caserne_chevalier.keys():
        if site_id in distance_sites:
            distance_sites.pop(site_id)
    for site_id in caserne_archer.keys():
        if site_id in distance_sites:
            distance_sites.pop(site_id)
    for site_id in caserne_geant.keys():
        if site_id in distance_sites:
            distance_sites.pop(site_id)
    for site_id, production in mines.items():
        if site_id in distance_sites and production[0] == production[2]:
            distance_sites.pop(site_id)
    for site_id, production in mine_fin.items():
        if production == 0:
            distance_sites.pop(site_id)
    for site_id in ennemie_tour.keys():
        if site_id in distance_sites:
            distance_sites.pop(site_id)

    # Calcule du site ne m'appartenant pas le plus proche
    if fuire == False:
        for site_id, distance in distance_sites.items():
            if min(distance_sites.values()) == distance:
                action1_b = site_id

# CONSTRUCTION
    if fuire == False:
        if len(tour) == 0:
            action1_a = "BUILD"
            action1_c = "TOWER"
        elif len(tour) == 1:
            for cle, val in tour.items():
                if val[0] <= 100:
                    action1_a = "BUILD"
                    action1_b = cle
                    action1_c = "TOWER"
                elif (gold - s_gold) < 3:
                    action1_a = "BUILD"
                    action1_c = "MINE"
                    for site_id, production in mines.items():
                        if production[0] < production[2]:
                            action1_a = "BUILD"
                            action1_b = site_id
                            action1_c = "MINE"
                elif len(caserne_chevalier) == 0:
                    action1_a = "BUILD"
                    action1_c = "BARRACKS-KNIGHT"
                elif len(caserne_geant) == 0 and len(ennemie_tour) > 0:
                    action1_a = "BUILD"
                    action1_c = "BARRACKS-GIANT"
                else:
                    action1_a = "BUILD"
                    action1_c = "MINE"
                    for site_id, production in mines.items():
                        if production[0] < production[2]:
                            action1_a = "BUILD"
                            action1_b = site_id
                            action1_c = "MINE"

# ENTRAINEMENT
    for chevalier_site in caserne_chevalier.keys():
        if len(chevalier) < 4:
            action2 = chevalier_site
        elif len(ennemie_tour) > 2:
            for geant_site in caserne_geant.keys():
                action2 = geant_site
        else:
            for chevalier_site in caserne_chevalier.keys():
                action2 = chevalier_site
                
# ACTION
    print("{} {} {}".format(action1_a, action1_b, action1_c))
    print("TRAIN {}".format(action2))