
#shuffle party - Round 930 div2 - A

t = int(input())

for _ in range(t):
    n = int(input())

    i = 0
    while 2**i<=n:
        i+=1
    if 2**i > n:
        i-=1
    print(2**i)