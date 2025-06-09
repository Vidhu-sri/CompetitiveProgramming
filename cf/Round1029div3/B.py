t = int(input())

for _ in range(t):

    n = int(input())

    res = [2]+[*range(3,n+1)]+[1]
    print(*res)