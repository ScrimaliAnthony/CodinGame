surface_n = int(input())
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    a = 0

    if v_speed <= -25 and v_speed > -30:
        a = 1
    if v_speed <= -30 and v_speed > -35:
        a = 2
    if v_speed <= -35 and v_speed > -40 or v_speed <= -35 and y > 1500:
        a = 3
    if v_speed <= -40 and y < 1500:
        a = 4

    print("0" , a)