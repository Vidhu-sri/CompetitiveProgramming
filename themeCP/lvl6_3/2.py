
t = int( input())


for _ in range(t):
    n,m,k = map(int,input().split())


    req = (m-1)*(n//m) +n%m
    req-=1 if n%m else 0 
    print('NO') if k>= req else print('YES')