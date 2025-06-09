# https://cses.fi/alon/task/1629



n = int(input())

movies = [tuple(map(int,input().split())) for _ in range(n)]

res = 1
selected = n-1
for i in range(n-2,-1,-1):
    if movies[selected][0] >= movies[i][1]:
        res+=1
        selected = i
print(res)
    




