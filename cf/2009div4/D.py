from collections import defaultdict
N = int(input())

for _ in range(N):
    n = int(input())
    coords = [tuple(map(int,input().split())) for _ in range(n)]
    coords = {'up':set([(x,y) for (x,y) in coords if y==1]), 'low':set([(x,y) for (x,y) in coords if y==0])}
    slopes = defaultdict(set)
    res = 0
    for coord in coords['up']:
        for down in coords['low']:
            if coord[0] == down[0]:
                #print(len(coords['low']), len(coords['up']))
                res += len(coords['low']) + len(coords['up']) - 2
                continue
            slope = (coord[1] - down[1])/(coord[0]-down[0])
            if -1/slope in slopes[coord]:
                res+=1
            slopes['coord'].add(slope)
    print(slopes)
    print(res)