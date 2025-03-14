t = int(input())


for _ in range(t):

    n,x = map(int,input().split())

    nums = list(map(int,input().split()))



    print('YES') if  sum(nums)== n*x else print('NO')