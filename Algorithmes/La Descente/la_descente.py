import sys
import math

# game loop
while True:
    dic = {}
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        dic[i] = mountain_h
    
    cible = max(dic, key=dic.get)

    print(cible)