t = int(input())

for _ in range(t):
    n,x = map(int,input().split())
    doors = list(map(int,input().split()))

    i,j = 0,n-1

    while not doors[j]:
        j-=1
    while not doors[i]:
        i+=1
    
    print('YES') if j-i+1 <=x else print('NO')
