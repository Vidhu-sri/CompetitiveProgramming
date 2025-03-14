


def check(max_penalty,colors,costs,k):
    strokes = k
    maxim = float('inf')

    for color, cost in zip(colors, costs):
        if color == "R":
            maxim = max(maxim, cost)
            continue

        if maxim <= max_penalty:
            continue

        if cost <= max_penalty:
            continue

        if not strokes:
            return False
        else:
            strokes -= 1
            maxim = 0
    
    return True


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    colors = input()
    costs = list(map(int, input().split()))

    res = None
    lo, hi = 0, max(costs)

    while lo <= hi:
        mid = lo +(hi-lo)//2

        if check(mid,colors,costs,k):
            res = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(res)