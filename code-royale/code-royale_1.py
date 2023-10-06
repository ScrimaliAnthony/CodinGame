import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

num_sites = int(input())
# sites = []
for i in range(num_sites):
    site_id, x, y, radius = [int(j) for j in input().split()]
    # site_info = {'site_id': site_id, 'x': x, 'y': y, 'radius': radius}
    # sites.append(site_info)

# game loop
next_site = 0
train = 0
midgame = False
next = False
barraqueT = "ARCHER"
while True:
    # touched_site: -1 if none
    gold, touched_site = [int(i) for i in input().split()]
    for i in range(num_sites):
        # ignore_1: used in future leagues
        # ignore_2: used in future leagues
        # structure_type: -1 = No structure, 2 = Barracks
        # owner: -1 = No structure, 0 = Friendly, 1 = Enemy
        site_id, ignore_1, ignore_2, structure_type, owner, param_1, param_2 = [int(j) for j in input().split()]
        if site_id == next_site and owner == 0:
            next = True
            if barraqueT == "ARCHER":
                barraqueT = "KNIGHT"

        if train + 2 == next_site:
            train += 1

    # reine = []
    num_units = int(input())
    for i in range(num_units):
        # unit_type: -1 = QUEEN, 0 = KNIGHT, 1 = ARCHER
        x, y, owner, unit_type, health = [int(j) for j in input().split()]
    

    if touched_site != -1 and midgame == False:
        next_site = touched_site
        train = next_site
        midgame = True
        next = True
    elif touched_site != -1 and midgame == True and next == True:
        next_site += 1
        next = False
    elif touched_site == -1 and midgame == True and next == True:
        next_site += 1
        next = False
    elif touched_site == -1 and midgame == False:
        next_site = 5
        next = True

    print("BUILD {} BARRACKS-{}".format(next_site, barraqueT))
    print("TRAIN {}".format(train))