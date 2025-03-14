from functools import cache
N = int(input())

@cache
def f(n):
    if n == 0:
        return True
    if n<0:
        return False
    
    res = False
    for i in {2020,2021}:
        subproblem = (n-i)
        if subproblem<0:
            continue
        res = res or f(subproblem)
    return res


for _ in range(N):

    n = int(input())

    if n< 2020:
        print('NO')
        
    elif f(n):
        print('YES')
    else:
        print('NO')