N = int(input())

for _ in range(N):
    n,k = list(map(int, input().split()))

    high,low = n,0
    # k, k+1,k+3, ... k+n-1
    best_delta = float('inf')
    
    while high>=low:
        mid = (low+high)//2

        c = k+mid
        ub = k+n-1
        diff = ub*(ub+1)//2 - c*(c+1) + k*(k-1)//2

        if abs(diff) < best_delta:
            best_delta = abs(diff)

        if diff >0:
            low = mid+1
        elif diff < 0:
            high = mid - 1
        else:
            break
    
    print(best_delta)
  


# 2,3       k = 2, n = 2
# 