from collections import deque

def solve(s):
    n = len(s)
    ans = [[-1] * 10 for _ in range(10)]

    for x in range(10):
        for y in range(10):
            # dist[pos][digit] = min insertions to reach pos in s with current digit
            dist = [[-1] * 10 for _ in range(n)]
            q = deque()

            # Start from 0
            if int(s[0]) != 0:
                continue  # impossible start
            dist[0][0] = 0
            q.append((0, 0))  # (position in s, last digit)

            while q:
                pos, digit = q.popleft()

                for step in [x, y]:
                    next_digit = (digit + step) % 10
                    if pos + 1 < n and int(s[pos + 1]) == next_digit:
                        if dist[pos + 1][next_digit] == -1:
                            dist[pos + 1][next_digit] = dist[pos][digit]
                            q.appendleft((pos + 1, next_digit))  # 0-cost move
                    if dist[pos][next_digit] == -1:
                        dist[pos][next_digit] = dist[pos][digit] + 1
                        q.append((pos, next_digit))  # insertion

            # Get min cost to reach the last position
            best = -1
            for d in range(10):
                if dist[n - 1][d] != -1:
                    if best == -1 or dist[n - 1][d] < best:
                        best = dist[n - 1][d]
            ans[x][y] = best

    return ans

string = input()
res= solve(string)

for i in range(len(res)):
    print(*res[i])