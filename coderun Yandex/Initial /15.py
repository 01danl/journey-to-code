import sys

def sol(res):

    is_const = True #1
    is_asc = True #2
    is_w_asc = True #3
    is_desc = True
    is_w_desc = True 
    
    for i in range(1, len(res)):
        if res[i-1] != res[i]: #1
            is_const = False
        if res[i-1] >= res[i]: #2
            is_asc = False
        if res[i-1] > res[i]:
            is_w_asc = False
        if res[i-1] <= res[i]:
            is_desc = False
        if res[i-1] < res[i]:
            is_w_desc = False

    if is_const:
        return "CONSTANT"
    if is_asc:
        return "ASCENDING"
    if is_w_asc:
        return "WEAKLY ASCENDING"
    if is_desc:
        return "DESCENDING"
    if is_w_desc:
        return "WEAKLY DESCENDING"
        
    return "RANDOM" 
def main():
    res = []
    
    while True:
        n = int(input())
        if n == -2000000000:
            break
        res.append(n)
    print(sol(res))
if __name__ == '__main__':
    main()
