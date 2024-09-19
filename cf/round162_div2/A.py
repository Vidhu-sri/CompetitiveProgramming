N = int(input())

for _ in range(N):

    n = int(input())
    if n>2:
        input()
        print('NO')
    elif n<2:
        input()
        print('YES')
    else:
        a,b = list(map(int,input().split(' ')))
        print('NO') if abs(a-b) == 1 else print('YES')
