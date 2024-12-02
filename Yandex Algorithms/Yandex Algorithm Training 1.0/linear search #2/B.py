def solution(res):
    is_constant = True
    is_ascending = True
    is_weakly_ascending = True
    is_descending = True
    is_weakly_descending = True

    for i in range(1, len(res)):
        if res[i] != res[i - 1]:
            is_constant = False
        if res[i] < res[i - 1]:
            is_weakly_ascending = False
        if res[i] <= res[i - 1]:
            is_ascending = False
        if res[i] > res[i - 1]:
            is_weakly_descending = False
        if res[i] >= res[i - 1]:
            is_descending = False

    if is_constant:
        return "CONSTANT"
    if is_ascending:
        return "ASCENDING"
    if is_weakly_ascending:
        return "WEAKLY ASCENDING"
    if is_descending:
        return "DESCENDING"
    if is_weakly_descending:
        return "WEAKLY DESCENDING"
    return "RANDOM"



res = []
while True:
    user = int(input())
    if user == -2 * 10**9: 
        break
    res.append(user)

print(solution(res))
