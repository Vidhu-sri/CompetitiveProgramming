
#Round 860 div2 - B

from collections import defaultdict
t = int(input())


for _ in range(t):
    m = int(input())

    lottery = []

    for _ in range(m):
        n_i = input()
        lottery.append(set(map(int,input().split())))
    last = defaultdict(list)
    lastx = set()
    for i in range(m-1,-1,-1):
        for p in lottery[i]:

            if p not in lastx:
                lastx.add(p)
                last[i].append(p)
    
    res = []
    flag = True
    for i in range(m):
        if not last[i]:
            flag = False
            break
        res.append(last[i][0])
    print(*res) if flag else print(-1)


    
