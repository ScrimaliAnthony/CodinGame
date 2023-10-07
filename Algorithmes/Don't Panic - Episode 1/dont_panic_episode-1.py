import sys
import math

dic = {}
ex_floor = 0
ex_pos = 0

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
for i in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    dic.update({elevator_floor : elevator_pos})

    ex_floor = exit_floor
    ex_pos = exit_pos

dic.update({ex_floor : ex_pos})

# game loop
action = "WAIT"
a = 0
b = 100
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])
    clone_pos = int(inputs[1]) 
    direction = inputs[2] 

    if clone_floor > a:
        a = clone_floor
        b = abs(clone_pos - dic[a])

    if clone_pos == width - 1 or clone_pos == 0:
        action = "BLOCK"
    elif b < abs(clone_pos - dic[a]):
            action = "BLOCK"
    else:
        action = "WAIT"
        
    print(action)