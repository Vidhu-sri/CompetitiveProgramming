    

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))

    uniq = len([set(nums)])

    visited = set()
    res = 0
    k = 0
    for i in range(n-1,-1,-1):
        if nums[i] not in visited:
            visited.add(nums[i])
        elif nums[i] in visited and len(visited) == uniq:
            res+=1
            visited = set([nums[i]])
            k+=1
    print(res)
            





