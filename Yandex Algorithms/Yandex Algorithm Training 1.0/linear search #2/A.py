def solution(lst):
    for i in range(1, len(lst)):
        if lst[i-1] < lst[i]:
            continue
        else:
            return False
    return True

res = list(map(int, input().strip().split()))

if solution(res):
    print("YES")
else:
    print("NO")
