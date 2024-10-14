N = int(input())

for _ in range(N):
    n,r = tuple(map(int,input().split()))
    nums = list(map(int,input().split()))
    res = 0
    rem_people, used_rows = 0,0
    
    for num in nums:
        res+= (num//2)*2
        used_rows += num//2
    rem_people = sum(nums) - res
    rem_rows = r - used_rows

    if rem_rows >= rem_people:
        print(res + rem_people)
    else: 
        to_add = 2*rem_rows - rem_people
        print(res+to_add)

    

               