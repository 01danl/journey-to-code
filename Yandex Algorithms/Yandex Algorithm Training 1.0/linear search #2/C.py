def solution(res,x):
    minim = 111111111
    difference = 0

    for n in res:
        difference = abs(x - n)
        if difference < minim:
            minim = difference
            save = n
    return save

n = int(input())
res = list(map(int, input().strip().split()))
x = int(input())

print(solution(res,x))
