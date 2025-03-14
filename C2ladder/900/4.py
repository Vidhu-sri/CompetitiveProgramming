N = int(input())


def bit_count(n):
    res = 0
    while n:
        res+= n&1
        n = n>>1
    return res


for _ in range(N):
    n = int(input())

    if n%2:
        print('YES')
    else:
        print('NO') if bit_count(n) ==1 else print('YES')





