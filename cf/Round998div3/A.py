N = int(input())

for _ in range(N):

    nums = list(map(int,input().split()))
    to_consider = [nums[0]+nums[1],nums[3]-nums[2],nums[2]-nums[1]]
    to_insert = max(to_consider,key=to_consider.count)
    nums.insert(2,to_insert)
    res =0
    for i in range(2,5):
        res+= (nums[i] == nums[i-1]+nums[i-2])
    print(res)
