N = int(input())

for _ in range(N):
    n = int(input())
    nums = list(map(int,input().split()))
    sum1 = [nums[i] for i in range(0,n,2)]
    sum2 = [nums[i] for i in range(1,n,2)]

    if not sum2:
        res =max(sum1)+len(sum1)
    else:
        res = max(max(sum1)+len(sum1), max(sum2)+len(sum2))
    print(res)