res1 = list(map(int, input().split()))
res2 = list(map(int, input().split()))

ans = set(res1) & set(res2) #if intersection
print(*sorted(ans))
