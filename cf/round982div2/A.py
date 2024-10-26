

N = int(input())

for _ in range(N):
    n = int(input())
    nums = [tuple(map(int,input().split())) for _ in range(n)]
    res = 2*sum(nums[0])
    max_x, max_y = nums[0]

    for i in range(1,n):
        x,y = nums[i]
        res+= 2*(max(0,x-max_x) + max(0,y-max_y))
        max_x = max(max_x,x)
        max_y = max(max_y,y)
    print(res)
    