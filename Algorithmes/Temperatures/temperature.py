import sys
import math

liste = []
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    t = int(i)
    liste.append(t)

result = min(liste, key=lambda x: (abs(x - 0), -x), default=0)

print(result)