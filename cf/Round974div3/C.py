

N = int(input())
for _ in range(N):


    n = int(input())
    nums = list(map(int, input().split()))

    total = sum(nums)
    maxim = max(nums)
    maxidx = nums.index(maxim) 

    target = n // 2 + 1

    needs = []

    for i in range(n):
        if i == maxidx:
            continue  
        a_i = nums[i]
        need = max(0, 2 * n * a_i - total + 1)
        needs.append(need)

    needs.sort()
    unhappy = 0

    if unhappy >= target:
        print(0)
    else:
        for need in needs:
            unhappy += 1
            if unhappy >= target:
                print(need)
                break
        else:
            print(-1)

        
