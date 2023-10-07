# To debug: print("Debug messages...", file=sys.stderr, flush=True)
import sys
import math

while True:
    dic_humain = {}

    dic_zombie = {}
    dic_next_zombie = {}

    dic_distance = {}

    next_pos_id = ""
    ash_x = ""
    ash_y = ""
    
    x, y = [int(i) for i in input().split()]

    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        dic_humain.update({ human_id : [ human_x, human_y ]})
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        dic_zombie.update({ zombie_id : [ zombie_x, zombie_y ]})
        dic_next_zombie.update({ zombie_id : [ zombie_xnext, zombie_ynext ]})

    # distance zombie et humain
    for human_id, human_pos in dic_humain.items():
        for zombie_id, zombie_pos in dic_zombie.items():
            dic_distance.update({ zombie_id : math.sqrt((human_pos[0] - zombie_pos[0])**2 + (human_pos[1] - zombie_pos[1])**2 )})

    # humain le plus proche d'un zombie
    distance = min(dic_distance.values())


    for zombie_id, val in dic_distance.items():
        if distance == val:
            next_pos_id = zombie_id
    
    for zombie_id, val in dic_zombie.items():
        if next_pos_id == zombie_id:
            ash_x = val[0]
            ash_y = val[1]

    print("{} {}".format(ash_x, ash_y))