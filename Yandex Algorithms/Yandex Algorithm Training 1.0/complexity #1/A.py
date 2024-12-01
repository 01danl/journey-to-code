t_room, t_cond = map(int, input().split())
res = input()

if res == "freeze":
    if t_room < t_cond:
        print(t_room)
    else:
        print(t_cond)

if res == "heat":
    if t_room < t_cond:
        print(t_cond)
    else:
        print(t_room)

if res == "auto":
    print(t_cond)

if res == "fan":
    print(t_room)
