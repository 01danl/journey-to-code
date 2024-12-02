def res(user):
    count = 0
    for i in range(1, len(user)):
        if i == len(user) - 1:
            break
        if user[i-1] < user[i] and user[i] > user[i+1]:
            count += 1
    return count
user = list(map(int, input().strip().split()))
print(res(user))

