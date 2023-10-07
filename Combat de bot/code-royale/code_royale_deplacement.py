import sys
import math

sites = []
num_sites = int(input())
for i in range(num_sites):
    site_id, x, y, radius = [int(j) for j in input().split()]
    site_info = {'site_id': site_id, 'x': x, 'y': y}
    sites.append(site_info)

while True:
    reine = []
    # touched_site: -1 if none
    gold, touched_site = [int(i) for i in input().split()]
    for i in range(num_sites):
        # structure_type: -1 = No structure, 2 = Barracks
        # owner: -1 = No structure, 0 = Friendly, 1 = Enemy
        site_id, ignore_1, ignore_2, structure_type, owner, param_1, param_2 = [int(j) for j in input().split()]


    num_units = int(input())
    for i in range(num_units):
        # unit_type: -1 = QUEEN, 0 = KNIGHT, 1 = ARCHER
        x, y, owner, unit_type, health = [int(j) for j in input().split()]
        reine_info = {"x": x, "y": y}
        reine.append(reine_info)

    for i in range(num_sites):
        Sx = sites[i]['x']
        Rx = reine[0]['x']
        Nx = Sx - Rx
        

    print("BUILD {} BARRACKS-KNIGHT".format(next_site))
    print("TRAIN {}".format(next_site))