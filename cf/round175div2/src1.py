

def solve(colors, penalties, n, k):
    def achievable(max_penalty):
        strokes_left = k
        largest_prev_R = float('inf')

        for color, penalty in zip(colors, penalties):
            if color == "R":
                largest_prev_R = max(largest_prev_R, penalty)
                continue

            # can I stretch the last Blue region?
            if largest_prev_R <= max_penalty:
                continue

            # ok can I skip painting this Blue as Red?
            if penalty <= max_penalty:
                continue

            if strokes_left == 0:
                return False
            else:
                strokes_left -= 1
                largest_prev_R = 0
        
        return True


    # binary search for the lowest possible penalty
    result = None
    lo, hi = 0, max(penalties)

    while lo <= hi:
        mid = (lo + hi) >> 1

        if achievable(mid):
            result = mid
            hi = mid - 1
        else:
            lo = mid + 1
    
    return result


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    colors = input()
    penalties = list(map(int, input().split()))
    print(solve(colors, penalties, n, k))