import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

while True:
    remaining_turns = int(input())

    d = ""

    if initial_ty > light_y:
        initial_ty -= 1
        d += "N"
    elif initial_ty < light_y:
        initial_ty += 1
        d += "S"

    if initial_tx > light_x:
        initial_tx += 1
        d += "W"
    elif initial_tx < light_x:
        initial_tx -= 1
        d += "E"

    print(d)